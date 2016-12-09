def _1lba(p) :
    syms = {'A':0,'C':1,'G':2,'T':3}
    i = 0
    k = 1
    p = p[::-1]
    for c in p :
        i = i+k*syms[c]
        k *= 4
    print i

_1lba("TTTCCGGAAAGAGAGTGAACGTCC")
