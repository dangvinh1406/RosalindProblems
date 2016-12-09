def sps(s,t) :
    if len(t) < len(s) :
        temp = s
        s = t
        t = temp
    i = 0;
    if s in t :
        return t
    while i < len(s) :
        if s[i:] == t[:len(s[i:])] :
            return s+t[len(s[i:]):]
        elif s[:len(s)-i] == t[len(t)-len(s[:len(s)-i]):] :
            return t+s[len(s)-i:]
        i += 1
    return s+t

def long(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    seqs = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seqs.append(seq_record.seq)
    i = 0    
    while i < len(seqs) :
        m = len(seqs[0])*2
        k = i
        lon = seqs[i]
        for j in range(len(seqs)) :
            if i != j :
                temp = sps(seqs[i],seqs[j])
                if len(temp) < m :
                    m = len(temp)
                    lon = temp
                    k = j
        seqs[i] = lon
        seqs.pop(k)
        if k < i :
            i -= 1
        if len(seqs) == 1 :
            break
    print seqs[0]
long("rosalind_long.txt")
