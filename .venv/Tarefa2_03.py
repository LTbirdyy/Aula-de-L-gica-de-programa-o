print('fale um numero entre 0 a 10:')
while True:
    resposta = int(input('Número:'))
    if resposta < 0 or resposta > 10:
        print('Opção inválida')
    else:
        print('Nota aceita:')
        break
print('Nota recebida')
