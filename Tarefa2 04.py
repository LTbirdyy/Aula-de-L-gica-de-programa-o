orcamento_total = float(input('Fale qual o valor total do orçamento:'))
cont = 0
custo_total = 0
while True:
    cont += 1
    servico = float(input(f'Fale o valor do {cont}º serviço:'))
    custo_total += servico
    orcamento_parcial = orcamento_total - custo_total
    if orcamento_parcial <= 0:
        print(f'Orçamento estourado  em \033[31mR${orcamento_parcial * -1}\033[0m')
        break
    else:
        print(f'Ainda restam \033[32mR${orcamento_parcial:.2f}\033[0m')
