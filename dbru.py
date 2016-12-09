def revComp(s) :
    t = ""
    com = {"A":"T","T":"A","G":"C","C":"G"}
    for c in s :
        t = com[c]+t
    return t

def dbru(filenameI,filenameO) :
    from Bio import SeqIO
    from Bio import Seq
    import collections
    file = open(filenameI)
    kmer = file.readlines()
    coll = []
    for i in range(len(kmer)):
        s = kmer[i][:len(kmer[i])-1]
        t = revComp(s)
        temp1 = "("+s[0:len(s)-1]+", "+s[1:len(s)]+")"
        temp2 = "("+t[0:len(t)-1]+", "+t[1:len(t)]+")"
        if temp1 not in coll :
            coll.append(temp1)
        if temp2 not in coll :
            coll.append(temp2)
    coll = sorted(coll)
    ff = open(filenameO,'w')
    for element in coll :
        #print element
        ff.write(element+"\n")
      
dbru("rosalind_dbru.txt","temp.txt")
