def getnumber(file):
    number = [int(i) for line in open(file, "r") for i in line.split()]
    return number

def large_ass_sum(numlist):
    return sum(numlist)


moo = getnumber("largeassnumber2.txt")

print large_ass_sum(moo)
