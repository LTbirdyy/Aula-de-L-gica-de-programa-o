print('Forneça os seguintes dados:')

while True:
    nome = input('Insira o nome(maior que três caracteres):')
    if len(nome) <= 3:
        print('Tente novamente')
    else:
        break
while True:
    idade = int(input('Insira a idade(entre 0 a 150)'))
    if idade > 150 or idade < 0:
        print('Tente novamente')
    else:
        break
while True:
    salario = float(input('Fale o seu salário(maior que 0)'))
    if salario <= 0:
        print('Tente novamente')
    else:
        break
while True:
    sexo = str(input('Fale o seu sexo[M/F]')).upper().strip()[0]
    if sexo in 'MF':
        break
    else:
        print('Tente novamente')
while True:
    estado = str(input('Indique qual estado civil você se encontra[S/C/V/D]')).upper().strip()[0]
    if estado in 'SCVD':
        break
    else:
        print('Tente novamente')
print('Cadastro realizado com sucesso')
