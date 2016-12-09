def lexf(symbols,n) :
    sym = symbols.split(" ")
    global li
    li = []
    p = []
    def rec(sym,p,n) :
        global li
        if len(p) == n :
            if p not in li :
                li.append(list(p))
        else :
            for i in range(len(sym)) :
                p.append(sym[i])
                rec(sym,p,n)
                p.pop()
    rec(sym,p,n)
    re = []
    for p in li :
        re.append("".join(map(str,p)))
    return re
def kmer(fastaFilename) :
    from collections import OrderedDict
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    seq = seq_collection[0]
    col = lexf("A C G T",4)
    dic = OrderedDict()
    for i in range(len(col)) :
        dic[col[i]] = 0
    for i in range(len(seq)) :
        if len(seq[i:i+4]) == 4 :
            dic[str(seq[i:i+4])] += 1
    kmer = list(dic.values())
    print " ".join(map(str,kmer))
