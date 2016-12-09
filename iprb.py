def iprb(k,m,n) :
    s = k + m + n
    a1 = k*1.0/s
    a2 = (m*1.0/s)*((k*1.0/(s-1)) + (3.0/4)*((m-1)*1.0/(s-1)) + 0.5*(n*1.0/(s-1)))
    a3 = (n*1.0/s)*(k*1.0/(s-1) + 0.5*(m*1.0/(s-1)))
    return a1 + a2 + a3