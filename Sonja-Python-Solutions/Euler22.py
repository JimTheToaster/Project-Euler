def getnames(file):
    name = [line.split() for line in open(file, "r")]
    names = name[0]
    while "," in names:
        names.remove(",")
    return sorted(names)

shots = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26 }

def get_name_value(names):
    for name in names:
        namesum = 0
        for char in name:
            namesum = namesum + shots.get(char)
        score = namesum*(names.index(name) + 1)
        names[names.index(name)] = score
    return sum(names)

print get_name_value(getnames("names.txt"))
