def hamm(s,t) :
    n = 0
    for i in range(len(s)) :
        if s[i] != t[i] :
            n += 1
    return (n*1.0)/len(s)
def pdst(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    n = len(seq_collection)
    mat = []
    for i in range(n) :
        mat.append([0]*n)
    for i in range(n) :
        for j in range(i,n) :
            if i != j :
                mat[i][j] = hamm(seq_collection[i],seq_collection[j])
                mat[j][i] = mat[i][j]
    
    for row in mat :
        print " ".join(map(str,["%.5f" %v for v in row]))

pdst("rosalind_pdst.fasta")
