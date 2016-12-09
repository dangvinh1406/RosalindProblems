def _3cba(filenameI,filenameO) :
        import collections
        file = open(filenameI)
        k = file.readline()
        k = int(k)
        test = file.readline()
        n = len(test)
        coll = collections.OrderedDict()
        for i in range (n - k+1):
                s1 = test[i:i + k]
                suf = s1[0:k-1]
                pre = s1[1:]
                if suf not in coll.keys():
                        coll[suf] = ' -> ' + pre
                else:
                        coll[suf] = coll[suf]+','+ pre

        coll = sorted(coll.items())
        ff = open(filenameO,'w')
        for element in coll :
                #print element[0]+element[1]
                ff.write(element[0]+element[1]+'\n')
      
_3cba("rosalind_3cba.txt","temp.txt")
