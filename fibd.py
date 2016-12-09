def fibd(n,m) :
    new = [1]
    while n > 0 :
        n = n-1
        k = len(new)-m
        if k < 0 :
            k = 0
        reproduce = sum(new[k:len(new)-1])       
        new.append(reproduce)
    print sum(new[len(new)-1-m:len(new)-1])
