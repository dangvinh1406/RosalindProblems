def splc(fastaFilename) :
    
    def deleteIntron(s,t) :
        i = 0
        while i < len(s)-len(t)+1 :
            if s[i:i+len(t)] == t :  
                s = s[:i]+s[i+len(t):]
            i += 1
        return s

    from Bio import SeqIO
    from Bio import Seq
    from Bio.Alphabet import IUPAC
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    DNA = seq_collection.pop(0)
    for intron in seq_collection :
        DNA = deleteIntron(DNA,intron)
    ARN = DNA.transcribe()
    print ARN.translate()

