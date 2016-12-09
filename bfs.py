def bfs(inputFile) :
    f = open(inputFile)
    st = f.readlines()
    col = []
    for s in st :
        n = s.split(" ")
        n[0] = int(n[0]); n[1] = int(n[1])
        col.append(n)
    arr = [0]*col[0][0]
    pre = [0]*(col[0][0]+1)
    vst = [0]*(col[0][0]+1)
    adj = []
    for i in range(col[0][0]+1) :
        adj.append(list([]))
    for i in range(1,col[0][1]+1) :
        adj[col[i][0]].append(col[i][1])

    queue = [1]
    while len(queue) > 0 :
        node = queue.pop(0)
        for i in range(len(adj[node])) :
            if vst[adj[node][i]] == 0 :
                pre[adj[node][i]] = node
                queue.append(adj[node][i])
                vst[adj[node][i]] = 1
            
    for i in range(1,col[0][0]) :
        node = i+1
        if vst[node] == 1 :
            while node != 1 :
                arr[i] += 1 
                node = pre[node]
        else :
            arr[i] = -1
    
    print " ".join(map(str,arr))
    f.close()
bfs("rosalind_bfs.txt")
