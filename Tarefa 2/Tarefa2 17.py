capital_inicial = float(input('Digite o valor inicial depositado:'))
taxa_juros_percentual = float(input('Digite a taxa de juros mensal em %:'))
periodo = int(input('Digite o período em meses:'))

# Converter os juros para decimal 50% -> 0.5
taxa_juros = taxa_juros_percentual / 100

print('Evolução do valor ao passar dos messes:')
for mes in range(1, periodo + 1):

    montante = capital_inicial * ((1 + taxa_juros) ** mes)
    print(f'No mês {mes}: R$ {montante:.2f}')
