def _7f(s,t) :
    for i in range(len(s)) :
        for j in range(len(s)-i) :
            if s[j:j+i] not in t :
                print s[j:j+i]
                return

