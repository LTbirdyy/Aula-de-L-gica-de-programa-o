quarto_termo = int(input('Digite o quarto termo da PA:'))
razao = int(input('Digite a razão da PA:'))
quantia_termos = int(input('Digite a quantidade de termos(valor inteiro e positivo):'))

# mesma logica que usei na questão 13
primeiro_termo = quarto_termo - (3 * razao)

soma = (quantia_termos / 2) * (2 * primeiro_termo + (quantia_termos - 1) * razao)

print(f'A soma dos {quantia_termos} primeiros termos da PA é: {soma}')
