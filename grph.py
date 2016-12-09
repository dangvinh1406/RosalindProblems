def grph(fastaFilename,k) :
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record)
    
    for seq1 in seq_collection :
        for seq2 in seq_collection :
            if seq2 is not seq1 :
                if seq1.seq[:k] == seq2.seq[len(seq2.seq)-k:] :
                    print "%s %s"%(seq2.id,seq1.id)
