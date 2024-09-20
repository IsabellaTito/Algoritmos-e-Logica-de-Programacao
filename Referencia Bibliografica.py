def referencia(nome):
    ref=[]
    ref.append(nome[-1].upper()+",")
    ref.append(" ".join(nome[0:len(nome)-1])+".")
    return ref

nome = input().lower().title().split()
for i in range(len(nome)):
    if nome[i] in ("Do","Da","De","Dos","Das","E"):
        nome[i]= nome[i].lower()
print(*referencia(nome))
