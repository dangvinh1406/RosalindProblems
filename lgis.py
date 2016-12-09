def lgis(inputFile) :
    f = open(inputFile)
    f.readline()
    perm = f.readline()
    d = perm.split()      
    for i in range(len(d)) :
        d[i] = int(d[i])
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]],key=len) 
                  + [d[i]])
    p = []
    for i in range(len(d)):
        p.append(max([p[j] for j in range(i) if p[j][-1] > d[i]] or [[]],key=len) 
                  + [d[i]])
    print " ".join(map(str,max(l,key=len)))
    print " ".join(map(str,max(p,key=len)))

lgis("rosalind_lgis.txt")
 

