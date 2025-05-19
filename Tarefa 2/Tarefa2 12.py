primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA: '))
limite= int(input('Tamanho da PA:'))
for c in range(primeiro, 1 + limite, razao):
        print(c, end=' ')
