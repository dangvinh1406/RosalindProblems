def mer(filename) :
    f = open(filename)
    f.readline()
    a = f.readline().split(" ")
    f.readline()
    b = f.readline().split(" ")
    for i in range(len(a)) :
        a[i] = int(a[i])
    mid = len(a)-1
    for i in range(len(b)) :
        a.append(int(b[i]))
    left = 0; right = len(a)-1;
    k = left; i = left; j = mid+1
    b = [0]*len(a)
    while k <= mid and j <= right :
        if a[k] <= a[j] :
            b[i] = a[k]; i += 1; k += 1
        else :
            b[i] = a[j]; i += 1; j += 1
    if j <= right :
        for h in range(j,right+1) :
            b[i] = a[h]
            i += 1
    if k <= mid :
        for h in range(k,mid+1) :
            b[i] = a[h]
            i += 1
    for s in range(left,right+1) :
        a[s] = b[s]

    tt = open("temp.txt","w")
    tt.write(" ".join(map(str,a)))
    #print " ".join(map(str,a))
    tt.close()
    f.close()
    
mer("rosalind_mer.txt")
            

    
                           
                           
