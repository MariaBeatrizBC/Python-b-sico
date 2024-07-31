#Calculando a média com if e else
nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a primeira nota: "))

media = (nota01 + nota02) / 2

if media >= 6.0:
    print("O aluno está aprovado! Sua nota final é", media)
else:
    print("O aluno está reprovado! Sua nota final é", media)