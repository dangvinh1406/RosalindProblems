def _7e(filename) :
    f = open(filename)
    s = f.readline()
    s = s[:len(s)-1]
    t = f.readline()
    t = t[:len(t)-1]
    seq_collection = [s,t]
    lengthSeq = []
    for seq in seq_collection :
        lengthSeq.append(len(seq))
    lmin = -1
    for l in range(len(lengthSeq)) :
        if lengthSeq[l] == min(lengthSeq) :
            lmin = l;break
    seqTemp = seq_collection.pop(lmin)
    comSubSeq = ""
    i = 0
    while i < len(seqTemp) :
        j = i+2
        flag = True
        while j <= len(seqTemp) :
            for seq in seq_collection :
                if seqTemp[i:j] not in seq :
                    flag = False;break
            if flag == False :
                break
            else :
                if len(seqTemp[i:j]) > len(comSubSeq) :
                    comSubSeq = seqTemp[i:j]
            j += 1
        i += 1
    print comSubSeq

_7e("rosalind_7e.txt")
