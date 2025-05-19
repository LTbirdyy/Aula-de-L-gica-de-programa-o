termo_1 = int(input('Digite o primeiro termo da PG: '))
razao = int(input('Digite a razão da PG:'))
quantia_termos = int(input('Digite a quantidade de termos (valor interio positivo):'))

print(f'Os {quantia_termos} primeiros termos da PG são:')
for c in range(quantia_termos):
    termos = termo_1 * (razao ** c)
    print(f'{termos}', end=' ')
