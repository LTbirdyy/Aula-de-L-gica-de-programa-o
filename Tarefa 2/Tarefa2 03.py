print('Escreva uma nota de 0 a 10.')
flag = 0
while flag == 0:
    nota = int(input('Fale a nota:'))
    if nota > 10 or nota < 0:
        print('Resposta inválida')
    else:
        flag = 1
print('Resposta aceita')
