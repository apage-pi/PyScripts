def factor_list(x):
    factors = []
    pairs = {}
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            if i not in factors:
                pairs[i] = []
                pairs[i].append(i)
                pairs[i].append(int(x/i))
                factors.append(i)
                factors.append(int(x/i))
            else:
                break
    #rint(factors)
    return pairs
    
#num = input("Number to list factors for: ")
#print("")
#print_factors(int(num))
