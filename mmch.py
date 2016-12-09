def mmch(fastaFilename) :            
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    seq = seq_collection.pop(0)
    nA = seq.count("A")
    nU = seq.count("U")
    nG = seq.count("G")
    nC = seq.count("C")
    pn = 1
    nAUm = min(nA,nU)
    nGCm = min(nG,nC)
    nAUM = max(nA,nU)
    nGCM = max(nG,nC)
    while nAUm > 0 or nGCm > 0 :
        if nAUm > 0:
            pn *= nAUM
            nAUm -= 1
            nAUM -= 1
        if nGCm > 0 :
            pn *= nGCM
            nGCM -= 1
            nGCm -= 1
    print pn

mmch("rosalind_mmch.txt")
