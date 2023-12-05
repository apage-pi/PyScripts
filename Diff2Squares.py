from math import sqrt
def is_square(n):
    return sqrt(n).is_integer()
def diff_2_squares(term1, term2):
    temp = ""
    term1v = term1[1]
    term1c = int(term1[0])
    temp = ""
    term2v = term2[1]
    for i in term2[0]:
        if(i.isdigit()):
            temp+=i
        else:
            pass
    term2c = int(temp)
    if is_square(term1c) == True:
        if is_square(term2c) == True:
            result = [[int(sqrt(term1c)), term1v], [int(sqrt(term2c)), term2v]]
        else:
            result = "none"
    else:
        result = "none"
    return result