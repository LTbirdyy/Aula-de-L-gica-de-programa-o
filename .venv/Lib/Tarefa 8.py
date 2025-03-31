print('Fale 4 números')
lista = list()
total_m = 0
total_g = 1
for c in range(1,5):
    numeros = float(input(f'Escolha um o {c}ª número:'))
    lista.append(numeros)
    total_m += numeros
    total_g *= numeros
#MEDIA PADRÃO
media = total_m/4
#MEDIA GEOMETRICA
media_g = total_g**0.25
#MEDIA HARMONICA
inversos = 1/lista[0] + 1/lista[1] + 1/lista[2] + 1/lista[3]
media_h = 4/inversos
#RESULTADO
print(f'A média dos {lista} é {media:.2f}, já a media geométrica seria {media_g:.2f}, e por fim {media_h:.2f}')
