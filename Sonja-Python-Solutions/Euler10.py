def primes(n):
    numarray = [True]*n
    numarray[0] = False
    numarray[1] = False
    for i in range(2,int(n**0.5)):
        if numarray[i]:
            for j in range(2*i,n, i):
                numarray[j] = False
    return [prime for prime in range(n) if numarray[prime]]
        
print sum(primes(2000001))
