def mprt(filename) :
    import urllib
    import urllib2
    #read contents in all ID fasta web page.
    f = open(filename)
    lines = f.readlines()
    mprt = open("mprt.txt","w")
    web_pg = ""
    for line in lines :
        aResp = urllib2.urlopen("http://www.uniprot.org/uniprot/"+line[:len(line)-1]+".fasta");
        web_pg += aResp.read()
    mprt.write(web_pg)
    mprt.close()
    #print all sequences to "mprt.txt"
    from Bio import SeqIO
    from Bio import Seq
    col = []
    for seq_record in SeqIO.parse("mprt.txt", "fasta") :
        col.append(seq_record)

    for k in range(len(col)) :
        idx = []
        for i in range(len(col[k].seq)-3) :
            if col[k].seq[i] == "N" :
                if col[k].seq[i+1] != "P" :
                    if col[k].seq[i+2] == "S" or col[k].seq[i+2] == "T" :
                        if col[k].seq[i+3] != "P" :
                            idx.append(i+1)
        if idx != [] :                    
            print lines[k][:len(lines[k])-1]
            print " ".join(map(str,idx))
    f.close()
mprt("rosalind_mprt.txt")
