def primes(n):
    primfac = []
    x = 2
    while x**2 <= n:
        while (n % x) == 0:
            primfac.append(x)
            n //= x
        x += 1
    if n > 1:
       primfac.append(n)
    return primfac
    
print primes(600851475143)
