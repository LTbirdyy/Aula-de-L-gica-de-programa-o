numeros = list()
total = 0
quantidade = int(input('Quantos números você quer escrever?'))
#COLENTANDO NÚMEROS
for c in range(0,quantidade):
    receber = float(input('Fale algum número:'))
    total += receber
    numeros.append(receber)
media = total/quantidade
# CALCULANDO VARIANCIA A DEPENDER DA ESCOLHA
contador = 0
variancia_t = 0
for d in range(0,quantidade):
    if contador == 0:
        variancia = (numeros[0] - media) ** 2
        variancia_t += variancia
    if contador > 0:
        variancia = (numeros[contador] - media) ** 2
        variancia_t += variancia
    contador += 1
variancia_t = variancia_t/quantidade
#CALCULO DESVIO PADRÃO
desvio_p = variancia_t ** 0.5
print('~' * 25 )
print(f'A média dos números {numeros} é {media:.0f}')
print(f'A variancia seria {variancia_t:.0f}')
print(f'Por fim o desvio padrão é {desvio_p:.0f}')
