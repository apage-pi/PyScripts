from math import sqrt
def is_square(n):
    return sqrt(n).is_integer()
def Diff2Squares(term1, term2):
    temp = ""
    term1v = ""
    for i in term1:
        if(i.isdigit()):
            temp+=i
        else:
            term1v+=i
    term1c = int(temp)
    temp = ""
    term2v = ""
    for i in term2:
        if(i.isdigit()):
            temp+=i
        else:
            term2v+=i
    term2c = int(temp)
    if is_square(term1c) == True:
        if is_square(term2c) == True:
            result = f"({int(sqrt(term1c))}{term1v} + {int(sqrt(term2c))}{term2v})({int(sqrt(term1c))}{term1v} - {int(sqrt(term2c))}{term2v})"
    return result