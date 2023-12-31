from math import sqrt
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"
    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.
    if common_divisor == 1:
        return (numer, denom)
    else:
        # Bunch of nonsense to make sure denominator is negative if possible
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                return(-reduced_num, -reduced_den)
            else:
                return (reduced_num, reduced_den)
        else:
            return (reduced_num, reduced_den)
def quadratic_function(a,b,c, d="x", e=""):
    '''Variable explanation:
    A - First Coefficent
    B - Second Coefficent
    C - Third Coefficient or Constant
    D - Variable in first term (default - x)
    E - Variablke in last term (default - none)'''
    if (b**2-4*a*c >= 0):
        x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
        # Added a "-" to these next 2 values because they would be moved to the other side of the equation
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1,den1) = simplify_fraction(a,mult1)
        (num2,den2) = simplify_fraction(a,mult2)
        if ((num1 > a) or (num2 > a)):
            # simplify fraction will make too large of num and denom to try to make a sqrt work
            return "No factorization"
        else:
            # Getting ready to make the print look nice
            if (den1 > 0):
                sign1 = "+"
            else:
                sign1 = ""
            if (den2 > 0):
                sign2 = "+"
            else:
                sign2 = ""
            factored = "({}{}{}{}{})({}{}{}{}{})".format(int(num1), d, sign1,int(den1), e, int(num2), d, sign2,int(den2), e)
            # remove "1" coefficients and replace them with the variable alone
            if "1{}".format(d) in factored:
                factored = factored.replace("1{}".format(d), d)
            if "1{}".format(e) in factored:
                factored = factored.replace("1{}".format(e), e)
            return factored
    else:
        # if the part under the sqrt is negative, you have a solution with i
        return "Solutions are imaginary"
    return

# This function takes in a, b, and c from the equation:
# ax^2 + bx + c
# and prints out the factorization if there is one

print(quadratic_function(7, 27, -4, "y", "b"))