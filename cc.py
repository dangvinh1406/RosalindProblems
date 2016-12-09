def cc(inputFile) :
    f = open(inputFile)
    st = f.readlines()
    col = []
    for s in st :
        n = s.split(" ")
        n[0] = int(n[0]); n[1] = int(n[1])
        col.append(n)
    vst = [1]*(col[0][0]+1)
    adj = []
    for i in range(col[0][0]+1) :
        adj.append(list([]))
    for i in range(1,col[0][1]+1) :
        adj[col[i][0]].append(col[i][1])
        adj[col[i][1]].append(col[i][0])

    #for c in adj :
        #print c
    
    cc = 0
    for k in range(1,len(vst)) :
        if vst[k] == 1 :
            vst[k] = 0
            cc += 1
            #print "cc", cc
            stack = [k]
            while len(stack) > 0 :
                node = stack.pop()
                vst[node] = 0
                #print node
                for i in range(len(adj[node])) :
                    if vst[adj[node][i]] == 1 :
                        stack.append(adj[node][i])
                        vst[adj[node][i]] = 0
    print cc            
    f.close()
cc("rosalind_cc.txt")
