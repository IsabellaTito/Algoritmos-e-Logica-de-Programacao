while True:
    idade = int(input())
    if idade == 0:
        break
    elif idade < 16 and idade > 0:
        print("Você não pode votar.")
    elif idade >= 18 and idade <= 70:
        print("Você tem a obrigatoriedade de votar.")
    elif idade > 70 or idade == 16 or idade == 17:
        print("Na sua idade, o voto é opcional.")
    elif idade < 0:
        print("Você ainda não nasceu.")
