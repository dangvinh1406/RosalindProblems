def subs(s,t) :
    i = 0
    index = []
    while i < len(s)-len(t)+1 :
        if s[i:i+len(t)] == t :
            index.append(i+1)
        i += 1
    print ' '.join(map(str,index))
        
