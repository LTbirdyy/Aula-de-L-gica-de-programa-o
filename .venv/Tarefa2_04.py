#ACEITAR APENAS VALORES >=100
while True:
    orcamento = int(input('Fale o seu orçamento, minimo R$ 100:'))
    if orcamento < 100:
        print('Orçamento inferior ao minimo.')
    else:
        print('Orçamento aceito.')
        break
print('Fale alguns valores de serviço e avisarei se eles cabem no seu orçamento.')
#VER SE CABE NO ORÇAMENTO
n_servico = 1
print('<>'*37)
while True:
    servico = int(input(f'Fale o valor do {n_servico}ª serviço:'))
    orcamento = orcamento - servico
    if orcamento >= 0:
        print(f'O serviço {n_servico} cabe no seu orçamento, restam\033[32m R${orcamento}\033[0m do seu orçamento.')
    if orcamento < 0:
        print('Orçamento ultrapassado')
        break
    n_servico += 1
print('<>'*37)
print(f'O orçamento foi ultrapassado em\033[31m R${orcamento * -1}\003[0m.')
