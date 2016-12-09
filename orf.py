def orf(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    from Bio.Alphabet import IUPAC
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    DNA = seq_collection.pop(0)
    i = 0
    pro = []
    while i < len(DNA) :
        if DNA[i:i+3] == "ATG" :
            j = i+3
            while j < len(DNA) :
                if DNA[j:j+3] == "TAG" or DNA[j:j+3] == "TGA" or DNA[j:j+3] == "TAA" :
                    if DNA[i:j].translate() not in pro :
                        pro.append(DNA[i:j].translate())
                    break
                j += 3
        i += 1
    DNA = DNA.reverse_complement()
    i = 0
    while i < len(DNA) :
        if DNA[i:i+3] == "ATG" :
            j = i+3
            while j < len(DNA) :
                if DNA[j:j+3] == "TAG" or DNA[j:j+3] == "TGA" or DNA[j:j+3] == "TAA" :
                    if DNA[i:j].translate() not in pro :
                        pro.append(DNA[i:j].translate())
                    break
                j += 3
        i += 1
    for p in pro :
        print p
    
orf("rosalind_orf.fasta")
