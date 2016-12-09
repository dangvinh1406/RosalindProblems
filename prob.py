def prob(inputFilename) :
    import math
    f = open(inputFilename)
    seq = f.readline()
    arr = (f.readline()).split(" ")
    for i in range(len(arr)) :
        arr[i] = float(arr[i])
    B = []
    for i in range(len(arr)) :
        proba = 1
        for c in seq :
            if c == "C" or c == "G" :
                proba = proba*(arr[i]/2)
            elif c == "A" or c == "T" :
                proba = proba*(1-arr[i])/2
        B.append(math.log(proba,10))
    print " ".join(map(str,B))

prob("rosalind_prob.txt")
