lettermap = {1:"one", 
             2:"two", 
             3:"three", 
             4:"four", 
             5:"five", 
             6:"six", 
             7:"seven", 
             8:"eight", 
             9:"nine", 
             10:"ten",
             11:"eleven",
             12:"twelve",
             13:"thirteen",
             14:"fourteen",
             15:"fifteen",
             16:"sixteen",
             17:"seventeen",
             18:"eighteen",
             19:"nineteen",
             20:"twenty",
             30:"thirty",
             40:"forty",
             50:"fifty",
             60:"sixty",
             70:"seventy",
             80:"eighty",
             90:"ninety"}

hund = len("hundred")
thou = len("thousand")
concat = len("and")

sum = 0

for n in range(1, 1001):
    if n in lettermap.keys():
        sum += len(lettermap.get(n))
    if n > 20 and n < 100 and n not in lettermap:
        k = str(n)
        first = int(k[0])
        second = int(k[1])
        sum = sum + (len(lettermap.get(first*10)) + len(lettermap.get(second)))
    elif n % 100 == 0 and n != 1000:
        k = str(n)
        first = int(k[0])
        sum = sum + len(lettermap.get(first)) + hund
    elif n > 100 and n < 1000 and n % 100 != 0:
        k = str(n)
        first = int(k[0])
        second = int(k[1])
        third = int(k[2])
        joint = int(str(second)+str(third))
        if joint > 10 and joint < 20:
            sum = sum + (len(lettermap.get(first)) + hund + concat + len(lettermap.get(joint)))
        elif second == 0:
            sum = sum + (len(lettermap.get(first)) + hund + concat + len(lettermap.get(third)))
        elif third == 0:
            sum = sum + (len(lettermap.get(first)) + hund + concat + len(lettermap.get(second*10)))
        else:
            sum = sum + (len(lettermap.get(first)) + hund + concat + len(lettermap.get(second*10)) + len(lettermap.get(third))) 
    elif n == 1000:
        sum = sum + len("one") + thou

print sum
