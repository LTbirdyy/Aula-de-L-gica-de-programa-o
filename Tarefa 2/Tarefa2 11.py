print('Forneça os dados pedidos para calcular o MDC e MMC:')

valor_1 = int(input('Fale o primeiro valor inteiro positivo:'))
salvo_1 = valor_1

valor_2 = int(input('Fale o segundo valor, também inteiro e positivo:'))
salvo_2 =valor_2

# Calcular MDC precisei usar o algoritmo de Euclides

while valor_2 != 0:
    resto = valor_1 % valor_2
    valor_1 = valor_2
    valor_2 = resto
mdc = valor_1

# Com o MDC a gente calcula o MMC so precisa usar os acumuladores criados no inicio

mmc = (salvo_1 * salvo_2) / mdc

print(f'O MDC é: {mdc}\nE o MMC é {mmc}')
