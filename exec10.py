#Função em python
soma = 0

def lerValor ():
    n1 = int(input("Digite o primeiro valor: "))
    return n1


def somar (n1, n2):
    soma = n1 + n2
    print("A soma dos valores é ", soma)


A = lerValor()
B = lerValor()
resultado = somar(A, B)