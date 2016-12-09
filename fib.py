def fib(n,k) :
    pairs = 0
    new = 1
    m1 = 0
    m2 = 0
    while n > 0 :
        n = n-1
        pairs = pairs+new
        m2 = m2+m1
        m1 = new
        new = m2*k
    print pairs
