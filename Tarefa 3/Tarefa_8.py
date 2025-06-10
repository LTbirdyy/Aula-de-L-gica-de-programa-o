# 8) Crie uma lista com pelo menos 20 números inteiros positivos menores do
# que 10. Então, o programa deverá mostrar quantas vezes cada um desses
# números aparece na lista. Mostre na tela o número e quantas vezes ele
# apareceu (mostre apenas uma vez para cada número diferente).
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 1, 5, 1, 3, 4, 5, 3, 2]

# Tirando as repetições dos números
lista_sem_repetidos = []
for index in range(0, len(lista)):
    if lista[index] not in lista_sem_repetidos:
        lista_sem_repetidos.append(lista[index])

# Quantidade de vezes que repetiu
lista_quantia_repetida = []
for index in range(0, len(lista_sem_repetidos)):
    lista_quantia_repetida.append(lista.count(lista_sem_repetidos[index]))

print(f'Na lista {lista} cada número apareceu na seguinte quatidade:')
# Mostrando quanto cada número se repetiu
for index in range(0, len(lista_sem_repetidos)):
    print(f'O número {lista_sem_repetidos[index]} apareceu {lista_quantia_repetida[index]}')
