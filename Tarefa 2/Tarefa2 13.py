razao = int(input('Digite a razão da PA:'))
terceiro_termo = int(input('Digite o terceiro termo da PA:'))
quantia_termos = int(input('Digite a quantidade de termos que deseja mostrar (maior que 3): '))

primeiro_termo = terceiro_termo - (2 * razao)

print(f'Os {quantia_termos} primeiros termos da PA são:')
for c in range(quantia_termos):
    termo = primeiro_termo + c * razao
    print(termo, end=' ')
