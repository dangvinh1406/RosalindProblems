def lgis(inputFile) :
    f = open(inputFile)
    f.readline()
    perm = f.readline()
    perm = perm.split()      
    for i in range(len(perm)) :
        perm[i] = int(perm[i])
    global incre,decre 
    incre = [];decre = [];
    global Max
    def increase(a) :
        if len(a) == 1 :
            return True
        for i in range(len(a)-1) :
            if a[i+1] < a[i] :
                return False
        return True

    def decrease(a) :
        if len(a) == 1 :
            return True
        for i in range(len(a)-1) :
            if a[i+1] > a[i] :
                return False
        return True
    
    def recI(a,perm,pflag,k) :
        global Max,incre
        if sum(pflag) > 0 :
            i = k
            while i < len(perm) :
                a.append(perm[i])
                pflag[i] = 0
                temp = perm.pop(i)
                if increase(a) :
                    if len(a) > Max :
                        Max = len(a)
                        incre = list(a)
                    recI(a,perm,pflag,i)
                perm.insert(i,temp)
                pflag[i] = 1
                a.pop()
                i += 1
    def recD(a,perm,pflag,k) :
        global Max,decre
        if sum(pflag) > 0 :
            i = k
            while i < len(perm) :
                a.append(perm[i])
                pflag[i] = 0
                temp = perm.pop(i)
                if decrease(a) :
                    if len(a) > Max :
                        Max = len(a)
                        decre = list(a)
                    recD(a,perm,pflag,i)
                perm.insert(i,temp)
                pflag[i] = 1
                a.pop()
                i += 1

    Max = 0;a = [];k = 0;pflag = [1]*len(perm)
    recI(a,perm,pflag,k)
    Max = 0;a = [];k = 0;pflag = [1]*len(perm)
    recD(a,perm,pflag,k)
    print " ".join(map(str,incre))
    print " ".join(map(str,decre))
lgis("rosalind_lgis.txt")
