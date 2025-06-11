import random
# Populando a lista
fitness = []
for tamanho in range(0, 1000):                     # ALTERAR O VALOR PARA MIL COMO PEDE A QUESTÃO DEPOIS DOS TESTES!!!
    fitness.append(random.random())

# Vendo menor valor
menor_valor = 0
index_menor_valor = 0

for interacao in range(1, 100_001):
    for index in range(0, len(fitness)):
        if index == 0:
            menor_valor = fitness[0]
        else:
            if menor_valor > fitness[index]:
                menor_valor = fitness[index]

    # Ao terminar de varrer a lista em busca do menor valor

    index_menor_valor = fitness.index(menor_valor)     # Salvar index dele para fazer alterações nos vizinhos

    # Antes de randomizar verificando quais eram os valores a serem mudados
    if interacao == 100_000:
        print('Antes de randomizar os vizinhos e menor valor')
        print(f'Lista como era:\n{fitness}')
        print(f'Antigo menor valor:\n{menor_valor}')
        print(f'Index do menor valor {index_menor_valor}')
        print()

    # Caso o menor valor esteja no fim
    if index_menor_valor == len(fitness) - 1:    # Verificando se ele tem o index do fim da lista
        fitness[index_menor_valor] = random.random()
        fitness[0] = random.random()                      # 0, pois é o primeiro valor
        fitness[index_menor_valor - 1] = random.random()

    # Caso o menor valor esteja no começo
    elif index_menor_valor == 0:               # Caso o primeiro valor seja o menor de todos
        fitness[index_menor_valor] = random.random()
        fitness[index_menor_valor + 1] = random.random()
        fitness[-1] = random.random()          # - 1, pois é o fim da lista

    # Caso o menor valor esteja no meio
    else:
        fitness[index_menor_valor] = random.random()
        fitness[index_menor_valor + 1] = random.random()
        fitness[index_menor_valor - 1] = random.random()


print('Depois de randomizar os vizinhos e menor valor')
print(f'Lista como ficou:\n{fitness}')
print(f'Novo valor aleatório para o menor valor: {fitness[index_menor_valor]}')
