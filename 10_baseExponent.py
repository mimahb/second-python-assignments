def Exponent(base, exp):
    result = 1
    for i in range(1, exp+1):
        result = result * base
    return result
base = 2
exp = 5
print(base,"raised to the power of ",exp,"is:", Exponent(base, exp),"\n","i.e (", base,"**",base, ")")