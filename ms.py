def mer(a,left,mid,right) :
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

def ms(filename) :
    f = open(filename)
    f.readline()
    A = f.readline().split(" ")
    for i in range(len(A)) :
        A[i] = int(A[i])
    left = 0; right = len(A)-1
    def mergeSort(A,left,right) :
        if left < right :
            mid = int((left+right)*0.5)
            mergeSort(A,left,mid)
            mergeSort(A,mid+1,right)
            mer(A,left,mid,right)
    
    mergeSort(A,left,right)
    tt = open("temp.txt","w")
    tt.write(" ".join(map(str,A)))
    tt.close()
    f.close()

ms("rosalind_ms.txt")
