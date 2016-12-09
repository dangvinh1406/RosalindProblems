def mirrorMatrix(matrix) :
    converted_matrix = {}
    for key in matrix:
        converted_matrix[key] = matrix[key]        
        try:
            converted_matrix[(key[1],key[0])] = matrix[(key[1],key[0])]
        except KeyError:
            converted_matrix[(key[1],key[0])] = matrix[key]
    return converted_matrix

def printMatrix(matrix) :
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '  '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

def printBS(BS) :
    aa =  "ACDEFGHIKLMNPQRSTVWY"
    for i in aa :
        for j in aa :
            print BS[(i,j)],
        print 
        
    
def glob(fastaFilename) :
    from Bio.SubsMat import MatrixInfo
    from Bio import SeqIO
    from Bio import Seq
    seq_collection = []
    for seq_record in SeqIO.parse(fastaFilename, "fasta") :
        seq_collection.append(seq_record.seq)
    s = seq_collection[0]
    t = seq_collection[1]
    sigma = 5
    #initialization
    BS = mirrorMatrix(MatrixInfo.blosum62)
    M = []
    for i in range(len(s)+1) :
        M.append([0]*(len(t)+1))
    for i in range(len(s)+1)[1:] :
        M[i][0] = M[i-1][0]-sigma
    for i in range(len(t)+1)[1:] :
        M[0][i] = M[0][i-1]-sigma

    #Matrix construction
    for i in range(1,len(s)+1) :
        for j in range(1,len(t)+1) :
            M[i][j] = max(M[i-1][j-1]+BS[(s[i-1],t[j-1])],M[i][j-1]-sigma,M[i-1][j]-sigma)
            
    print M[len(s)][len(t)]
glob("rosalind_glob.txt")



