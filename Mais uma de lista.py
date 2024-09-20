n = int(input())
if n == 0:
    print("Lista vazia - O valor de S eh zero")
elif n < 0:
    print("O valor informado para N foi negativo")
else:
    A = []
    S=0
    for i in range(n):
        num = int(input())
        A.append(num)
    if n%2==0:
        for j in range(n//2):
            S += (A[j]-A[(n-1)-j])**2
        print("S =",S)
    else:
        for j in range(n//2):
            S += (A[j]-A[(n-1)-j])**2
        S+=(A[int((n-1)/2)])**2
        print("S =",S)
