def revp(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    seq = seq_collection[0]
    i = 0
    while i < len(seq) :
        j = 4
        while j <= 12 :
            if i+j > len(seq):
                break
            seqTemp = seq[i:i+j]
            revSeqTemp = seqTemp.reverse_complement()
            if seqTemp == revSeqTemp :
                print "%s %s"%(i+1,j)
            j += 1
        i += 1

            
    
