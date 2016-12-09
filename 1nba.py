def _1mba(i,k) :
    syms = ['A','C','G','T']
    p = ""
    while k > 0 :
        p = syms[i%4] + p
        i = int(i)/4
        k -= 1
    return p

def ham(s,t,d) :
    for i in range(len(s)) :
        if s[i] != t[i] :
            d -= 1
            if d < 0 :
                return 0
    return 1

def _1nba(t,d) :
    k = len(t)
    for i in range(4**k) :
        temp = _1mba(i,k)
        if ham(t,temp,d) == 1 :
            print temp


_1nba("TGAAACCTACC",2)
    


