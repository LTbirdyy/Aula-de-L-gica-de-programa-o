cont = 0
total = 0

print('Fale quantos números quiser para eu fazer a média deles, caso queira parar escreva algum número negativo:')
while True:
    n1 = int(input('Fale algum número:'))
    if n1 < 0:
        break
    if n1 > 0:
        cont += 1
        total += n1
        media = total/cont_poositivo
print(f'A média dos valores dados é {media}')
