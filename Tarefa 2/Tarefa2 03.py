print('Escreva uma nota de 0 a 10.')
while True:
    nota = int(input('Fale a nota:'))
    if nota > 10 or nota < 0:
        print('Resposta inválida')
    else:
        break
print('Resposta aceita')