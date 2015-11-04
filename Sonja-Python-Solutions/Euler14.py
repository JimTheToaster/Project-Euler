def find_number(size):
    startlist = [i for i in range(0, size)]
    coll_list = sorted([[collatz_length(j), j] for j in startlist])
    return coll_list[len(coll_list)-1][1]

def collatz_length(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        count+=1
    return count

print find_number(1000000)
