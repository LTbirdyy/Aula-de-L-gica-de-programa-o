cont_positivo = 0
cont_negativo = 0
flag = 1
print('Escreva quantos números quiser e direi quantos números negativos e positivos você escreveu(para parar digite 0)')
while flag != 0:
    numero = int(input('Fale qualquer número:'))
    if numero > 0:
        cont_positivo += 1
    elif numero < 0:
        cont_negativo += 1
    else:
        flag = 0
print(f'De um total de {cont_negativo + cont_positivo} números você escreveu {cont_positivo} números positivos'
      f' e {cont_negativo} negativos.')
