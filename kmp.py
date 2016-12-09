def kmp(fastaFilename) :            
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    seq = seq_collection.pop(0)
    T = [0]*len(seq)
    pos = 2
    cnd = 0
    while pos < len(seq) :
        if seq[pos-1] == seq[cnd] :
            cnd += 1
            T[pos] = cnd
            pos += 1
        elif cnd > 0 :
            cnd = T[cnd]
        else :
            T[pos] = 0
            pos += 1
    f = open("temp.txt",'w')
    f.write(" ".join(map(str,T)))

    
import time
tic = time.clock()
#kmp("temp.fasta")
kmp("rosalind_kmp.fasta")
toc = time.clock()
print toc - tic
