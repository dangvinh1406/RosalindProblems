def lcsq(fastaFilename) :
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    s = seq_collection[0]
    t = seq_collection[1]
    sigma = -1
    BS = { ('A','A') : 5,('A','T') :-5,('A','G') :-5,('A','C') :-5,
           ('T','T') : 5,('T','A') :-5,('T','G') :-5,('T','C') :-5,
           ('C','C') : 5,('C','A') :-5,('C','G') :-5,('C','T') :-5,
           ('G','G') : 5,('G','T') :-5,('G','A') :-5,('G','C') :-5 }
    M = []
    for i in range(len(s)+1) :
        M.append([0]*(len(t)+1))
    for i in range(len(s)+1)[1:] :
        M[i][0] = M[i-1][0]-sigma
    for i in range(len(t)+1)[1:] :
        M[0][i] = M[0][i-1]-sigma
        
    for i in range(1,len(s)+1) :
        for j in range(1,len(t)+1) :
            M[i][j] = max(M[i-1][j-1]+BS[(s[i-1],t[j-1])],M[i][j-1]-sigma,M[i-1][j]-sigma)

    s_aln = ""
    i = len(s); j = len(t)
    
    while i >= 1 and j >= 1 :
        if M[i][j] == M[i-1][j-1]+BS[(s[i-1],t[j-1])]:
            s_aln = s[i-1]+s_aln
            i = i-1; j = j-1
        elif M[i][j] == M[i-1][j]-sigma :
            i = i-1
        elif M[i][j] == M[i][j-1]-sigma :
            j = j-1
        else :
            print 'should not happen'
            break

    print s_aln

lcsq("rosalind_lcsq.txt")
