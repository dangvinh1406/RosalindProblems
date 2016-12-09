def ham1(s,t) :
    f = 0
    for i in range(len(s)) :
        if s[i] != t[i] :
            f += 1
            if f > 1 :
                return 0
    if f == 1 :
        return 1
    return 0
def corr(fastaFilename) :            
    from Bio import SeqIO
    from Bio import Seq
    seqs = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seqs.append(seq_record.seq)
    cor = []
    inc = []
    while len(seqs) > 0 :
        temp = seqs.pop(0)
        if temp in seqs or temp.reverse_complement() in seqs:
            while temp in seqs :
                seqs.remove(temp)
            while temp.reverse_complement() in seqs :
                seqs.remove(temp.reverse_complement())
            cor.append(temp)
        else :
            inc.append(temp)

    for r in inc :
        for i in range(len(cor)) :
            if ham1(r,cor[i]) :
                print r+"->"+cor[i]
            elif ham1(r,cor[i].reverse_complement()) :
                print r+"->"+cor[i].reverse_complement()
                
corr("rosalind_corr.txt")
