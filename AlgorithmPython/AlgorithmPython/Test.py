
Matrix = []

for i in range(3):
    (a,b,c) = (int(x) for x in raw_input().split())
    Matrix.append(list((a,b,c)))

def printM(M):
    for i in range(3):
        for j in range(3):
            print Matrix[i][j],
        print

def dfs():
    n = 0
    for i in range(3):
        num = 0
        left = 15
        pos = 0
        for j in range(3):
            if Matrix[i][j] != 0:
                num += 1
                left -= Matrix[i][j]
            else:
                pos = j
        if num == 2:
            Matrix[i][pos] = left
            n += 1
    for i in range(3):
        num = 0
        left = 15
        pos = 0
        for j in range(3):
            if Matrix[j][i] != 0:
                num += 1
                left -= Matrix[j][i]
            else:
                pos = j
        if num == 2:
            Matrix[pos][i] = left
            n += 1
    left = 15
    num = 0
    pos = 0
    for i in range(3):
        if Matrix[i][i] != 0:
            num += 1
            left -= Matrix[i][i]
        else:
            pos = i
    if num == 2:
        Matrix[pos][pos] = left
        n+=1
    left = 15
    num = 0
    pos = 0
    for i in range(3):
        if Matrix[i][2 - i] != 0:
            num += 1
            left -= Matrix[i][2 - i]
        else:
            pos = i
    if num == 2:
        Matrix[pos][2 - pos] = left
        n+=1
    return n        

if Matrix[1][1] == 0:
    Matrix[1][1] = 5          
while dfs() > 0:
    pass
Zero = False
for i in range(3):
    for j in range(3):
        if Matrix[i][j] == 0:
            Zero = True

if Zero:
    print 'Too Many'
else:   
    printM(Matrix)


    
                


            