print('Me fale um número para ser a base e outro para ser o expoente')
base = int(input('Número para base:'))
expoente = int(input('Número para o expoente:'))
flag = 0
resultado = 1
while flag != expoente:
    flag += 1
    resultado *= base
print(resultado)
