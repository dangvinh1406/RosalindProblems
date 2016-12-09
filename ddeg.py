def ddeg(inputFile) :
    f = open(inputFile)
    st = f.readlines()
    col = []
    for s in st :
        n = s.split(" ")
        n[0] = int(n[0]); n[1] = int(n[1])
        col.append(n)
    de = [0]*(col[0][0]+1)
    arr = [0]*col[0][0]
    adj = []
    for i in range(col[0][0]+1) :
        adj.append(list([]))
    for i in range(1,col[0][1]+1) :
        de[col[i][0]] += 1
        de[col[i][1]] += 1
        adj[col[i][0]].append(col[i][1])
        adj[col[i][1]].append(col[i][0])
    for i in range(col[0][0]) :
        for a in adj[i+1] :
            arr[i] += de[a] 
        
    print " ".join(map(str,arr))
    f.close()
ddeg("rosalind_ddeg.txt")
