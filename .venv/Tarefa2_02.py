cont_positivo = 0
cont_negativo = 0
print('Fale alguns números caso queira parar escreva 0')
while True:
    resposta = int(input('Fale um número:'))
    if resposta > 0:
        cont_positivo += 1
    if resposta < 0:
        cont_negativo += 1
    if resposta == 0:
        break
print(f'Você escreveu {cont_positivo} números positivos e {cont_negativo} números negativos')
