from math import gcd
def GCFFactor(terms):
    coefficients = []
    vars = []
    temp = 0
    temp2 = ""
    gcf = 0
    similar_vars = ""
    finlist = []
    for i in terms:
        coefficients.append(i[0])
        vars.append(i[1])
    gcf = gcd(*coefficients)
    var_sets = [{*s} for s in vars]
    result_set = var_sets[0]
    for var_set in var_sets[1:]:
        result_set.intersection_update(var_set)
    gcv = ''.join(sorted(list(result_set)))
    for i in terms:
        if gcv in i[1]:
            if len(i) == 3:
                i[2] -= 1
            else:
                i[1].replace(gcv, "")
        i[0] /= gcf
        i[0] = int(i[0])
    fin = f"{gcf}("
    for i in terms:
        if len(i) == 3:
            finlist.append(str(i[0]))
            finlist.append(str(i[1]))
            finlist.append(f"^(str({i[2]}))")
            if i != len(i):
                if "-" not in str(i[0]):
                    finlist.append("+")
        else:
            finlist.append(str(i[0]))
            finlist.append(str(i[1]))   
            if i != len(terms):
                try:
                    if "-" not in str(terms[temp+1][0]):
                        finlist.append("+")
                except IndexError:
                    finlist.append("+")
        temp += 1
    for i in finlist:
        fin += i
    fin = fin[:-1]
    fin += ")"
    return fin  
print(GCFFactor([[3, "x"], [366, ""], [-162, ""]]))
