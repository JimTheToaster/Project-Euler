def tripledigitpalins():
    s = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            s.append(multiply(i, j))
    d = map(ispalindrome, s)
    print max(d)

def ispalindrome(num):  
    n = str(num)  
    while len(n)>1:  
        #print n  
        if n[0] != n[-1]:  
            return 0  
        n = n[1:-1]  
    return num 
            
def multiply(x,y):
    return x*y

tripledigitpalins()
