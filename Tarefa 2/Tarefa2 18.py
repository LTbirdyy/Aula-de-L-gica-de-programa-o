aplicacao = float(input('Digite o valor da aplicação que sera depositado todo mês:'))
juros_mensal = float(input('Digite a taxa de juros mensal em %:'))
periodo = int(input('Digite o total de meses:'))

# convertendo para decimal
taxa = juros_mensal / 100

montante = 0

print('Mês | Montante (R$) | Juros (R$)')
print('-' * 30)

for mes in range(1, periodo + 1):

    # juros sobre o montante acumulado
    juros = montante * taxa

    # adicionar juros e nova aplicação para atualizar os valores

    montante += juros + aplicacao
    total_aportes = aplicacao * mes
    total_juros = montante - total_aportes

# Tabela pra ficar bonitinho

    print(f'{mes:>3} | {montante:>13.2f} | {total_juros:>10.2f}')
