matr = list(map(int,input().split()))
m = []
for i in range(matr[0]):
    m.append(list(map(int,input().split())))
for j in range(matr[1]):
    for i in range(matr[0]):
        if j%2==0:
            if m[i][j] == 1:
                print('Desliga o farol cidadao ( ._.)')
            else:
                print('Queria que todo mundo fosse assim')
        else:
            if i == 0:
                if m[matr[0]-1][j] == 1:
                    print('Desliga o farol cidadao ( ._.)')
                else:
                    print('Queria que todo mundo fosse assim')
            else:
                if m[matr[0]-(i+1)][j] == 1:
                    print('Desliga o farol cidadao ( ._.)')
                else:
                    print('Queria que todo mundo fosse assim')
