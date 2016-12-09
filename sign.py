def sign(n) :
    global li
    li = []
    p = []
    num = 0
    i = -n
    perm = []
    while i <= n :
        if i != 0 : perm.append(i)
        i += 1
    def rec(perm,p) :
        global li
        if len(p) == n :
            if p not in li :
                li.append(list(p))
        else :
            for i in range(len(perm)) :
                temp = perm.pop(i)
                p.append(temp)
                k = perm.index(-temp)
                perm.pop(k)
                rec(perm,p)
                perm.insert(k,-temp)
                perm.insert(i,p.pop())
    rec(perm,p)
    print len(li)
    for p in li :
        print " ".join(map(str,p))
