#Tabuada
n1 = int(input('Escolha um números para eu fazer a tabuada dele'))
for c in range (1,11):
    resultado = n1 * c
    print(f'{n1} x {c:2d} = {resultado:3d}')
