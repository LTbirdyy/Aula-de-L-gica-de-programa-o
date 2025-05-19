provas = int(input('Digite o número de provas:'))

soma = 0
soma_dos_quadrados = 0

for i in range(1, provas + 1):
    nota = float(input(f'Digite a nota da prova {i}: '))
    soma += nota
    soma_dos_quadrados += nota * nota

# Cálculo da média
media = soma / provas

# Cálculo do desvio padrão usei a formula do desvio padrão
variancia = (soma_dos_quadrados / provas) - (media * media)

# Raiz quadrada sem usar o sqrt() do math
desvio_padrao = variancia ** 0.5

print(f'Média das notas: {media:.2f}')
print(f'Desvio padrão: {desvio_padrao:.2f}')
