def aspc(n,m) :
    from operator import mul    
    from fractions import Fraction

    def nCk(n,k): 
        return int(reduce(mul,(Fraction(n-i,i+1) for i in range(k)),1))

    re = 0
    while m <= n :
        re += nCk(n,m)%1000000
        m += 1
    print re%1000000

aspc(1855,845)
