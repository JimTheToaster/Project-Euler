def pascal(n, k):
    return factorial(n+k)/(factorial(n)**2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print pascal(20, 20)
