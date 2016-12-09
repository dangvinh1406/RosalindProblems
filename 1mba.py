def _1mba(i,k) :
    syms = ['A','C','G','T']
    p = ""
    while k > 0 :
        p = syms[i%4] + p
        i = int(i)/4
        k -= 1
    print p

_1mba(5520,8)
