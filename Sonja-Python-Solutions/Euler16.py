def powerdigitsum(n):
    number = [int(i) for i in str(2**n)]
    return sum(number)

print powerdigitsum(1000)
