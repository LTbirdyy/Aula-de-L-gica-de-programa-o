razao = int(input('Digite a razão da PG:'))
terceiro_termo = int(input('Digite o terceiro termo da PG:'))
quantia_termos = int(input('Digite a quantidade de termos (valor maior que 3):'))

# Descobrir primeiro termo igual as outras questões la
termo_1 = terceiro_termo / (razao ** 2)

print(f'Os {quantia_termos} primeiros termos da PG são:')

# Acumulador
soma = 0

# copiado da tarefa anterior so modifiquei o int(termo) para ficar mais bonito
for c in range(quantia_termos):
    termo = termo_1 * (razao ** c)
    print(f'{int(termo)}', end=' ')
    soma += termo

print(f'\nSoma dos {quantia_termos} primeiros termos da PG: {soma}')
