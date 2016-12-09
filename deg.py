def deg(inputFile) :
    f = open(inputFile)
    st = f.readlines()
    col = []
    for s in st :
        n = s.split(" ")
        n[0] = int(n[0]); n[1] = int(n[1])
        col.append(n)
    arr = [0]*col[0][0]
    for i in range(1,col[0][1]+1) :
        for j in range(2) :
            arr[col[i][j]-1] += 1 
    print " ".join(map(str,arr))

deg("rosalind_deg.txt")
