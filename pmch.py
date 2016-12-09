def pmch(fastaFilename) :            
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    seq = seq_collection.pop(0)
    nA = seq.count("A")
    nC = seq.count("C")
    pn = 1
    while nA > 0 or nC > 0 :
        if nA > 0:
            pn *= nA
            nA -= 1
        if nC > 0 :
            pn *= nC
            nC -= 1
    print pn
          
