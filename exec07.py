#Utilizando elif
idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Não pode votar!")
elif idade < 18:
    print("O voto é opcional!")
elif idade <= 70:
    print("O voto é obrigatório!")
else:
    print("O voto é opcional!")