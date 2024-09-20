mat = list(map(int,input().split()))
m1,m2,resl=[],[],[]
for i in range(2*mat[0]):
    if i>=0 and i < mat[0]:
        m1.append(list(map(int,input().split())))
    else:
        m2.append(list(map(int,input().split())))
for i in range(mat[0]):
    l=[]
    for j in range(mat[1]):
        soma = m1[i][j] + m2[i][j]
        l.append(soma)
    resl.append(l)
for i in range(mat[0]):
    print(*resl[i])    
