cont_positivo = 0
cont_negativo = 0
print('Escreva quantos números quiser e direi quantos números negativos e positivos você escreveu(para parar digite 0)')
while True:
    numero = int(input('Fale qualquer número:'))
    if numero > 0:
        cont_positivo += 1
    elif numero < 0:
        cont_negativo += 1
    else:
        break
print(f'De um total de {cont_negativo + cont_positivo} números você escreveu {cont_positivo} números positivos e {cont_negativo} negativos.')
