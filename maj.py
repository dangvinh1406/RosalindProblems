def majorE(x,A) :
    if x not in A :
        return 0
    elif len(A) == 2 :
        if sum(A) == x+x :
            return 2
        else :
            return 1
    elif len(A) == 1 :
        return 1
    elif len(A) <= 0 :
        return 0
    else :
        return majorE(x,A[:int(len(A)*0.5)])+majorE(x,A[int(len(A)*0.5):])
        
def maj(filename) :
    f = open(filename)
    n = f.readline().split(" ")
    n = [int(n[0]),int(n[1])]
    re = []
    for i in range(n[0]) :
        r = -1
        A = f.readline().split(" ")
        for i in range(n[1]) :
            A[i] = int(A[i])
        for x in A :
            if majorE(x,A) > n[1]*0.5 :
                r = x
                break
        re.append(r)

    #tt = open("temp.txt","w")
    #tt.write(" ".join(map(str,re)))
    print " ".join(map(str,re))

maj("rosalind_maj.txt")
