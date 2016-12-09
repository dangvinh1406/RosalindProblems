def writeSetToFile(S,fi) :
    fi.write("%s%s%s\n"%("{",", ".join(map(str,S)),"}"))


def seto(fileNameI,fileNameO) :
    f1 = open(fileNameI)
    n = int(f1.readline())
    Uni = set(range(1, n+1))
    A = f1.readline()
    B = f1.readline()
    A = (A[1:len(A)-2]).split(", ")
    B = (B[1:len(B)-2]).split(", ")
    for i in range(len(A)) :
        A[i] = int(A[i])
    
    for i in range(len(B)) :
        B[i] = int(B[i])
    A = set(A)
    B = set(B)
    f2 = open(fileNameO,'w')
    writeSetToFile(list((A | B)),f2)
    writeSetToFile(list((A & B)),f2)
    writeSetToFile(list((A - B)),f2)
    writeSetToFile(list((B - A)),f2)
    writeSetToFile(list((Uni - A)),f2)
    writeSetToFile(list((Uni - B)),f2)
    f1.close()
    f2.close()
    
seto("rosalind_seto.txt","f2.txt")    
             
