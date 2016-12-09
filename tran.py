def tran(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    s = seq_collection[0]
    t = seq_collection[1]
    transi = 0
    transv = 0
    nu = {"A":"G","G":"A","C":"T","T":"C"}
    for i in range(len(s)) :
        if nu[s[i]] == t[i] :
            transi += 1
        elif s[i] != t[i] :
            transv += 1
    print (transi*1.0)/transv

tran("rosalind_tran.fasta")
