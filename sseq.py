def sseq(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    s = seq_collection[0]
    t = seq_collection[1]
    j = 0
    idx = []
    for i in range(len(s)) :
        if s[i] == t[j] :
            idx.append(i+1)
            j += 1
            if j == len(t) :
                break
    print " ".join(map(str,idx))

