def spec(filename) :
    wP = {"A":71.03711,
        "C":103.00919,
        "D":115.02694,
        "E":129.04259,
        "F":147.06841,
        "G":57.02146,
        "H":137.05891,
        "I":113.08406,
        "K":128.09496,
        "L":113.08406,
        "M":131.04049,
        "N":114.04293,
        "P":97.05276,
        "Q":128.05858,
        "R":156.10111,
        "S":87.03203,
        "T":101.04768,
        "V":99.06841,
        "W":186.07931,
        "Y":163.06333}
    f = open(filename)
    spec = f.readlines()
    for i in range(len(spec)) :
        spec[i] = float(spec[i])
    i = len(spec)-1
    s = ""
    while i > 0 :
        w = spec[i]-spec[i-1]
        for p in wP :
            if abs(wP[p]-w) <  0.0001 :
                s = p+s
                break
        i -= 1
    print s
    f.close()

spec("rosalind_spec.txt")
