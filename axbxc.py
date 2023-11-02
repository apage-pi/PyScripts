from FactorList import print_factors as pfactors
def splitphrase(phrasei):
    phrase = phrasei
    split1s = 0
    split1e = phrase.index("^")
    split1 = phrase[split1s:split1e]
    split2s = int(phrase.index("(")) + 1
    split2e = int(phrase.index(")"))
    split2 = phrase[split2s:split2e]
    split3 = phrase[split2e + 1]
    split3i = phrase.index(split3)
    split4s = split3i + 1
    if split3 == '-':
        try:
            split4e = phrase.index("+")
        except ValueError:
            split4e = phrase.index("-", split3i+1)
    elif split3 == "+":
        try:
            split4e = phrase.index("-")
        except ValueError:
            split4e = phrase.index("+", split3i+1)
            print(split4e)
    split4 = phrase[split4s:split4e] 
    split5 = phrase[split4e]
    split6s = split4e + 1
    split6e = len(phrase)
    split6 = phrase[split6s:split6e]
    split = [split1, split2, split3, split4, split5, split6]
    return split
def axbxc(phrase):
    split = splitphrase(phrase)
    term1 = split[0]
    exponent = split[1]
    sign1 = split[2]
    term2= split[3]
    sign2 = split[4]
    term3 = split[5]
    if exponent != 2:
        print("The first term is not squared!")
        print("Either it cannot be factored this way,")
        print("or you have not factored out enough things.")
        return 0
    