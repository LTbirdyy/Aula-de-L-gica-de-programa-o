# Precisei usar chat gpt esse, não tava conseguindo fazer a lógica sozinho
numero = int(input('Digite um número inteiro positivo:'))

binario = ""
n = numero

while n > 0:
    resto = n % 2
    binario = str(resto) + binario  # acrescenta o bit à esquerda
    n = n // 2  # divide o número por 2 (parte inteira)

print(f'O número {numero} em binário é: {binario}')
