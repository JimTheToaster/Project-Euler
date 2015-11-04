def sum_squares(size):
    sumsqlist = [i**2 for i in range(1, size+1)]
    return sum(sumsqlist)

def square_sum(size):
    sqsumlist = [i for i in range(1, size+1)]
    return (sum(sqsumlist))**2

def difference(num1, num2):
    return num1 - num2


print difference(square_sum(100), sum_squares(100))
