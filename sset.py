def sset(n) :
    import math
    re = 1
    i = 1
    while i <= n :
        re += math.factorial(n)/(math.factorial(n-i)*math.factorial(i))
        re %= 1000000
        i += 1
    print re

