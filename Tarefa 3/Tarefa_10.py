from random import randint

# Fazendo com duas listas
# Populando lista
print(f'{'FAZENDO COM 2 LISTAS':-^30}')
lista = []
lista_positivo = []
for i in range(0, 30):
    lista.append(randint(-20, 20))

# Retirando valores negativos
for index in range(0, 30):
    if lista[index] > 0:
        lista_positivo.append(lista[index])

# Resultados
print('Lista completa: ')
print(*lista, sep=', ')
print('\nlista somente com os positivos: ')
print(*lista_positivo, sep=', ')

# Fazendo com uma só lista
print(f'\n{'FAZENDO COM 1 LISTA':-^30}')
# populando lista
lista = []
print('Lista completa:')
for i in range(0, 30):
    valor = randint(-20, 20)      # Diferente da forma de cima aqui eu separo os números positivos dos negativos
    if valor > 0:                    # antes de sequer adicionar na lista assim não precisando fazer uma nova lista
        lista.append(valor)

    print(valor, end=', ')

print('\nlista somente com os positivos:')
print(*lista, sep=', ')
