num = int(input())
vet = []
for i in range(num):
    tam = int(input())
    vet.append(tam)
vet.sort()
soma = 0
for j in range(num-1):
    dif = vet[j+1]-vet[j]
    if dif > 1:
        soma += (dif-1)
print(soma)
