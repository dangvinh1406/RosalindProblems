def ins(filename) :
    f = open(filename)
    f.readline()
    a = f.readline().split(" ")
    for i in range(len(a)) :
        a[i] = int(a[i])
    count = 0
    for i in range(1,len(a)) :
        k = i
        while k > 0 and a[k] < a[k-1] :
            temp = a[k-1]
            a[k-1] = a[k]
            a[k] = temp
            k = k-1
            count += 1
    print count

ins("rosalind_ins.txt")
