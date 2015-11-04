def evenfibs(size):
    fiblist = []
    for i in range(0, size):
        if fib(i) < 4000000 and fib(i) % 2 == 0:
            fiblist.append(fib(i))
    print fiblist
    return sum(fiblist)
    
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print evenfibs(34)
