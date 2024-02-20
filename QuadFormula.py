from math import *
def quadform(a=1, b=1, c=1, x="x"):
    result = 0
    temp1 = b**2
    temp2 = 4*a*c
    negb = -1 * b
    disc = temp1 - temp2
    if disc > -1 :
        temp4 = 2*a
        result = '''              _________
                    {} = {} +/- \/{}
                    -------------------
                            {}'''.format(x, str(negb), str(disc), str(temp4))
    else:
        result = "No Real Solution"
    return result