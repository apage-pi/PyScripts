from fractions import Fraction
def gcf(numbers):
    gcf = 1
    abs_numbers = [abs(i) for i in numbers]
    large = max(abs_numbers)
    if numbers[0] >= 0:
        for i in range(large, 1, -1):
            if all(number % i == 0 for number in abs_numbers) == True:
                gcf = i
                break
    else:
        for i in range(-large, -1):
            if all(number % i == 0 for number in abs_numbers) == True:
                gcf = i
                break
    return gcf
def factors(x):
    factors = []
    for i in range(1, abs(int(x)) + 1):
        if x % i == 0:
            factors.append(i)
    return factors
def remove_duplicates(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output
def fractions(lista, listb):
    fractions = []
    lista = [float(i) for i in lista]
    listb = [float(i) for i in listb]
    for i in lista:
        for j in listb:
            fractions.extend([i / j, -i / j])
    fractions = remove_duplicates(fractions)
    return(fractions)
def synthetic_division(coefficients, divisor):
    results = [float(coefficients[0])]
    for i in range(len(coefficients) - 1):
        results.append(results[-1] * divisor + coefficients[i + 1])
    return(results)
def factor1(coefficients):
    factors_leading = factors(coefficients[0])
    factors_constant = factors(coefficients[-1])
    possible_roots = fractions(factors_constant, factors_leading)
    for i in possible_roots:
        results = synthetic_division(coefficients, i)
        if results[-1] == 0:
            results.pop(-1)
            return([-i, results])
            break
    else:
        return False
def factor(coefficients):
    gcf1 = gcf(coefficients)
    coefficients = [coefficient / gcf1 for coefficient in coefficients]
    polynomial = coefficients
    roots = []
    while factor1(polynomial) != False:
        roots.append(factor1(polynomial)[0])
        polynomial = factor1(polynomial)[1]
    polynomial = [int(term) for term in polynomial]
    gcf2 = gcf(polynomial)
    polynomial = [term / gcf2 for term in polynomial]
    for i in range(len(roots)):
        if roots[i] % 1 != 0:
            numerator = []
            denominator = []
            slash = False
            for j in str(Fraction(roots[i]).limit_denominator()):
                if j == '/':
                    slash = True
                if slash == False:
                    numerator.append(j)
                elif j == '/':
                    pass
                else:
                    denominator.append(j)
            frac = (int("".join(numerator)), int("".join(denominator)))
            roots[i] = (frac[1], frac[0])
        else:
            roots[i] = (1, int(roots[i]))
    if gcf1 == 1:
        answer = []
    else:
        answer = [str(gcf1)]
    for i in roots:
        answer.append("(%sx + %s)" % (i[0], i[1]))
    string = ["("]
    for i in range(len(polynomial)):
        if i == len(polynomial) - 2:
            string.append("%sx + " % (polynomial[i]))
        elif i == len(polynomial) - 1:
            string.append("%s" % (polynomial[i]))
        else:
            string.append("%sx^%s + " % (polynomial[i], len(polynomial) - i - 1))
    string.append(")")
    string = "".join(string)
    if len(polynomial) > 1:
        answer.append(string)
    answer = "".join(answer)
    return(answer)
term_number = int(input("How many terms are in your polynomial? "))
coefficients = []
coefficients.append(int(input("What is the highest degree term's coefficient? ")))
for i in range(term_number - 2):
    coefficients.append(int(input("What is the next highest degree term's coefficient? ")))
coefficients.append(int(input("What is the constant? ")))
print(factor(coefficients))