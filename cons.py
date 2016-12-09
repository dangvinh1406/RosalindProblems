def cons(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    length = []
    for seq in seq_collection :
        length.append(len(seq))
    lth = min(length)
    A = [];C = [];G = [];T = []
    consensus = ""
    for i in range(lth) :
        nA = 0;nC = 0;nG = 0;nT = 0
        for seq in seq_collection :
            if seq[i] == "A" :
                nA += 1
            elif seq[i] == "C" :
                nC += 1
            elif seq[i] == "G" :
                nG += 1
            else : 
                nT += 1
        A.append(nA);C.append(nC);G.append(nG);T.append(nT)
        if nA == max(nA,nC,nG,nT):
            consensus += "A"
        elif nC == max(nA,nC,nG,nT): 
            consensus += "C"
        elif nG == max(nA,nC,nG,nT): 
            consensus += "G"
        else :
            consensus += "T"
    print consensus
    print "A: %s"%(" ".join(map(str,A)))
    print "C: %s"%(" ".join(map(str,C)))
    print "G: %s"%(" ".join(map(str,G)))
    print "T: %s"%(" ".join(map(str,T)))
