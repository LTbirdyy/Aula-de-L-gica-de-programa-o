valor = float(input('Fale o valor do produto:'))
desconto = float(input('Fale a porcentagem do desconto:'))
desconto = desconto / 100
desconto = valor * desconto
final = valor - desconto
print(f'O valor incial é de {valor}, com um desconto de {desconto}% o valor final fica {final}.')
