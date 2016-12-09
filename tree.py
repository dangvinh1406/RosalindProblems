def tree(inputFilename) :
    f = open(inputFilename)
    n = int(f.readline())
    numOfLines = sum(1 for line in f)
    print n
    print n-1-numOfLines

tree("rosalind_tree.txt")
