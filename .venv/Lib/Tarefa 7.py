quantidade = int(input('Escolha a quantidade de números para fazer a média'))
numeros = 0
lista = list()
for c in range(0,quantidade):
    escolha = int(input('Escreva um número:'))
    lista.append(escolha)
    numeros += escolha
resultado = numeros / quantidade
print(f'A média dos números {lista} resulta em {resultado}')

