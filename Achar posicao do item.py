lista = []
conte = 0
while True:
    num = int(input())
    if num == 0 and len(lista)<3:
        print("você deve digitar pelo menos 3 números antes do 0.")
    elif num == 0:
        break
    elif num != 0 and num in lista:
        print("número já existe na lista, tente outro.")
    elif num!=0:
        lista.append(num)
print(lista)
print("o maior elemento da lista é:", max(lista),"e ele se encontra na posição:", lista.index(max(lista)))
print("o menor elemento da lista é:", min(lista),"e ele se encontra na posição:", lista.index(min(lista))) 
