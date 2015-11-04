def factorize(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
def triangulize(n):
    return n * (n+1) /2
    
def find_tri():
    triangle_number = 1
    factors = set()
    while len(factors) < 501:
        factors = factorize(triangulize(triangle_number))
        triangle_number += 1
    return triangulize(triangle_number-1)

print find_tri()
