def lexv(symbols,n) :
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
                if p not in li :
                    li.append(list(p))
                rec(sym,p,n)
                p.pop()
    rec(sym,p,n)
    f = open("temp.txt",'w')
    for p in li :
        f.write("%s\n"%("".join(map(str,p))))


lexv("V E U R G B Q O D T J X",4)
