def bins(filename) :
    f = open(filename)
    f.readline()
    f.readline()
    A = f.readline().split(" ")
    B = f.readline().split(" ")
    for i in range(len(A)) :
        A[i] = int(A[i])
    for i in range(len(B)) :
        B[i] = int(B[i])
    
    R = []
    for alpha in B :
        idx = -1
        l = 0; r = len(A)-1
        while l <= r :
            m = int((l+r)*0.5)
            if A[m] == alpha :
                idx = m+1
                break
            elif A[m] > alpha :
                r = m-1
            else :
                l = m+1
        R.append(idx)
    print " ".join(map(str,R))

bins("rosalind_bins.txt")
