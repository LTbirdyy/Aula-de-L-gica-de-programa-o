
from random import randint
dados = []
lista_positiva = []
lista_negativa = []

# Sorteando valores
for valores in range(0, 20):         # Delimitar em 20 números como pediu
    dados.append(randint(-10, 10))

# Separando valores positivos
for index in range(0, 20):
    if dados[index] > 0 or dados[index] == 0:
        lista_positiva.append(dados[index])

    # Separando agora os negativos
    else:
        lista_negativa.append(dados[index])

# Respostas
print(f'Lista original:\n{dados}\nSeparando os valores em positivos e negativos temos:')

print(*lista_positiva, sep=', ')

print('-' * 60)

print(*lista_negativa, sep=', ')
