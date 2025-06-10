# Criei essa função só para facilitar a separação das respostas ela não influência em nada o código
def linha():
    print('-'*40)


lista = [460, 800, 300, 400]
tamanho_lista = len(lista)
print(f'Na lista:\n{lista}')
linha()

# Calculando a MÉDIA
soma_total = 0
for valores in lista:
    soma_total += valores

media = soma_total / tamanho_lista

print(f'A média da lista é aproximadamente:\n{media:.2f}')
linha()

# Calculando a MEDIANA

# Ordenando a lista para poder fazer mediana
lista = sorted(lista)

# Caso o len(lista) seja impar
if tamanho_lista % 2 != 0:
    index_mediana = int((tamanho_lista+1) / 2) - 1    # Precisa subtrair por 1 pelo fato da contagem iniciar no 0
    mediana = lista[index_mediana]

# Caso o len(lista) seja par
else:
    index_elemento_1 = int((tamanho_lista/2) - 1)          # Por se tratar de uma lista par não tem um meio 'exato'
    index_elemento_2 = int(((tamanho_lista/2) + 1) - 1)    # Para isso fazemos a média entre os dois termos no meio

    # Média dos elementos resulta na mediana
    mediana = ((lista[index_elemento_1] + lista[index_elemento_2])/2)

print(f'A mediana é:\n{mediana}')
linha()

# Calculando a MODA
mais_repetido = []  # Precisa ser uma lista pela possibilidade de mais de um valor como moda

# Verificando as vezes que cada número aparece (mds)
print(f'A moda dessa lista é:')
for index in range(0, tamanho_lista):
    if lista.count(lista[index]) != 1:          # Aqui verifica se a quantidade de vezes que tal número da lista aparceu é maior que 1
        if lista[index] not in mais_repetido:   # Nessa parte evita de aparecer mais de uma vez o mesmo número na resposta ex: 3,3
            mais_repetido.append(lista[index])  # ADD FINALMENTE os valores cetos

# Caso todos os números tenham a mesma ocorrência
if not mais_repetido:
    print('Amodal, pois os números aparecem a mesma quantidade de vezes.')

print(*mais_repetido, sep='-')
linha()

# Calculando VARIÂNCIA
lista_variancia = []     # Criei uma lista para dividir o processo do cálculo
soma_total = 0           # Acumular a soma dos valores da lista_variancia
variancia = 0            # So pq o IDE tava reclamando
for index in range(0, tamanho_lista):
    passo1_variancia = (lista[index] - media) ** 2
    lista_variancia.append(passo1_variancia)

    # Somar os diferentes valores e dividir pela quantia de valores
    soma_total += lista_variancia[index]
    variancia = soma_total / tamanho_lista     # As duas lista vão ter sempre o mesmo tamanho

print(f'A variância é:\n{variancia}')
linha()

# Calculando DESVIO PADRÃO
desvio = variancia ** 0.5
print(f'O desvio padrão é aproximadamente:\n{desvio:.2f}')
linha()
