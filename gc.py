def gc(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record)
    maxi = -1
    GCcon = 0
    for i in range(len(seq_collection)) :
        GCnum = 0
        for c in seq_collection[i].seq :
            if c == "C" or c == "G" :
                GCnum += 1
        GCconNow = (GCnum*1.0)/len(seq_collection[i].seq)
        if GCconNow > GCcon :
            GCcon = GCconNow
            maxi = i
    print seq_collection[maxi].id
    print GCcon*100
