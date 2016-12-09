def perm(n) :
    import itertools
    se = range(n)
    for i in range(n) :
        se[i] = se[i]+1
    ls = list(itertools.permutations(se))
    print len(ls)
    for tup in ls :
        print ' '.join(map(str,tup))
        
    
            
    
                
