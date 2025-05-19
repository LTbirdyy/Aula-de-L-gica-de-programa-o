orcamento_total = float(input('Fale qual o valor total do orçamento:'))
cont = 0
custo_total = 0
flag = 0
while flag == 0:
    # Saber quantidade de serviços
    cont += 1
    # Recebendo valor do serviço
    servico = float(input(f'Fale o valor do {cont}º serviço:'))
    print(f'Serviço de R${servico} sendo adicionado')
    # Salvando em um acumulador
    custo_total += servico

    # Vendo se vai caber no orçamento estabelecido
    orcamento_parcial = orcamento_total - custo_total

    if orcamento_parcial < 0:
        print(f'Orçamento estourado  em \033[31mR${orcamento_parcial * -1}\033[0m:')

        flag = 1

    elif orcamento_parcial == 0:
        print('\033[31mOrçamento já foi atingido:\033[0m')

        flag = 1

    else:
        print(f'Ainda restam \033[32mR${orcamento_parcial:.2f}\033[0m')

    print('-' * 40)

print('Não é possivel pedir mais nenhum serviço')
