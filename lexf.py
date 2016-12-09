def lexf(symbols,n) :
    sym = symbols.split(" ")
    global li
    li = []
    p = []
    def rec(sym,p,n) :
        global li
        if len(p) == n :
            if p not in li :
                li.append(list(p))
        else :
            for i in range(len(sym)) :
                p.append(sym[i])
                rec(sym,p,n)
                p.pop()
    rec(sym,p,n)
    for p in li :
        print "".join(map(str,p))

