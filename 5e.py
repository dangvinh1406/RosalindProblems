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
        
    
def _5e(s,t,sigma) :
    from Bio.SubsMat import MatrixInfo
    #initialization
    BS = mirrorMatrix(MatrixInfo.blosum62)
    M = []
    for i in range(len(s)+1) :
        M.append([0]*(len(t)+1))
    for i in range(len(s)+1)[1:] :
        M[i][0] = M[i-1][0]-sigma
    for i in range(len(t)+1)[1:] :
        M[0][i] = M[0][i-1]-sigma
    printBS(BS)
    #Matrix construction
    for i in range(1,len(s)+1) :
        for j in range(1,len(t)+1) :
            M[i][j] = max(M[i-1][j-1]+BS[(s[i-1],t[j-1])],M[i][j-1]-sigma,M[i-1][j]-sigma)

    s_aln = ""
    t_aln = ""
    i = len(s); j = len(t)
    printMatrix(M)
    
    while i >= 1 and j >= 1 :
        if M[i][j] == M[i-1][j-1]+BS[(s[i-1],t[j-1])]:
            t_aln = t[j-1]+t_aln
            s_aln = s[i-1]+s_aln
            i = i-1; j = j-1
        elif M[i][j] == M[i-1][j]-sigma :
            s_aln = s[i-1]+s_aln
            t_aln = '-'+t_aln
            i = i-1
        elif M[i][j] == M[i][j-1]-sigma :
            s_aln = '-'+s_aln
            t_aln = t[j-1]+t_aln
            j = j-1
        else :
            print 'should not happen'
            break

    if i > 0 :  
        while i > 0 :
            s_aln = s[i-1]+s_aln
            t_aln = '-'+t_aln
            i = i-1
    elif j > 0 :
        while j > 0 :
            s_aln = '-'+s_aln
            t_aln = t[j-1]+t_aln
            j = j-1

    print M[len(s)][len(t)]
    print s_aln
    print t_aln

##f = open("rosalind_5e.txt")
##s = f.readline()
##s = s[:len(s)-1]
##t = f.readline()
##t = t[:len(t)-1]
##_5e(s,t,5)
##f.close()
_5e("MEANLY","PLEASANTLY",5)

