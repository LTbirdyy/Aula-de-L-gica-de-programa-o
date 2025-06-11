# ATENÇÃO O TAMANHO DA LISTA ESTÁ EM 1000 COMO FOI PEDIDO NA QUESTÃO, PORÉM O OUTPUT FICA ENORME
from random import randint
# Populando lista
lista = []
for index in range(0, 1000):                   # MUDAR VALOR DEPOIS (DNV ESTÁ EM 1000 CUIDADO)
    lista.append(randint(0, 1))          # Adicionando valores na lista
    lista.insert(index, lista[index] * 100)   # Multiplicando valor
    lista.pop(index + 1)                      # Elimando o valor antigo na lista

# Automatizar número de intervalos
limite_intervalos = int(len(lista)/5)
lista_resultados = []
inicio = 0
fim = 5
soma_intervalo = 0
for intervalos in range(0, limite_intervalos):   # O limite aq do for é feito pegando o tamanho da lista e / 5
    print('-'*30)                                # Caso queira mudar o tamanho dos intervalos precisa alterar o valor da
    for valores in lista[inicio:fim]:            # variável(facilitou os testes)
        print(valores, end=', ')
        soma_intervalo += valores  # Somar os valores desse intervalo

    else:          # O else serve para que assim que o loop seja conlcuido em cima venha pra ca
        print()
        print('-'*30)
        lista_resultados.append(soma_intervalo)
        print(f'Soma do {intervalos + 1}ª intervalo:\n{soma_intervalo}')

    soma_intervalo = 0    # Precisa limpar a variâvel para a próxima soma
    inicio += 5           # Como os intervalos são de 5-5 precisamos ir crescendo
    fim += 5              # os limitadores

print(f"{'RESUMO':-^20}")
print(f'A lista com a soma dos intervalos é: {lista_resultados}')
