def _3dba(filenameI,filenameO) :
        import collections
        file = open(filenameI)
        kmer = file.readlines()
        coll = collections.OrderedDict()
        for i in range(len(kmer)):
                s = kmer[i]
                suf = s[0:len(s)-2]
                pre = s[1:len(s)-1]
                if suf not in coll.keys():
                        coll[suf] = ' -> ' + pre
                else:
                        coll[suf] = coll[suf]+','+ pre

        coll = sorted(coll.items())
        ff = open(filenameO,'w')
        for element in coll :
            print element[0]+element[1]
            ff.write(element[0]+element[1]+'\n')
      
_3dba("rosalind_3dba.txt","temp.txt")
