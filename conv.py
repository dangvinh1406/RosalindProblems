def conv(filename) :
    
    def convertToFloat(s) :
        for i in range(len(s)) :
            s[i] = float(s[i])
    def convertToString(s) :
        for i in range(len(s)) :
            s[i] = str(s[i])
    def countFrequency(s,value) :
        count = 0
        idx = []
        for i in range(len(s)) :
            if s[i] == value :
                count += 1
                idx.append(i)
        for i in idx :
            s.pop(i)
        return count
    
    f = open(filename)
    s1 = f.readline().split(" ")
    s2 = f.readline().split(" ")
    convertToFloat(s1)
    convertToFloat(s2)
    Mdiff = []
    for i in range(len(s1)) :
        for j in range(len(s2)) :
            Mdiff.append(round(s1[i]-s2[j],5))
    convertToString(Mdiff)
    mF = 0
    mV = 0
    while len(Mdiff) > 0 :
        temp = Mdiff[0]
        tempF = countFrequency(Mdiff,temp)
        if tempF > mF :
            mF = tempF
            mV = temp
    
    print mF
    print mV

conv("rosalind_conv.txt")
