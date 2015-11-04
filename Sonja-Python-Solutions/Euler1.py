def multiples(size):
    numlist = []
    for i in range(1, size):
        if i%3 == 0 or i%5 == 0:
            numlist.append(i)
    print sum(numlist)

multiples(1000)
