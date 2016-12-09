def iev(data) :
    a = data.split(" ")
    for i in range(len(a)) :
        a[i] = int(a[i])
    b = [1.0, 1.0, 1.0, 0.75, 0.5, 0]
    s = 0
    for i in range(0,6) :
        s += 2*a[i]*b[i]
    print s

iev("18596 18810 19932 19802 19636 18794")
