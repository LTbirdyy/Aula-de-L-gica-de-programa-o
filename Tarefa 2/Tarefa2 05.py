print('Forneça os seguintes dados:')

flag = 0
while flag == 0:
    nome = input('Insira o nome(maior que três caracteres):')
    if len(nome) <= 3:
        print('Tente novamente')
    else:
        flag = 1
print('-'*40)

flag = 0
while flag == 0:
    idade = int(input('Insira a idade(entre 0 a 150)'))
    if idade > 150 or idade < 0:
        print('Tente novamente')
    else:
        flag = 1
print('-'*40)

flag = 0
while flag == 0:
    salario = float(input('Fale o seu salário(maior que 0)'))
    if salario <= 0:
        print('Tente novamente')
    else:
        flag = 1
print('-'*40)

flag = 0
while flag == 0:
    sexo = str(input('Fale o seu sexo[M/F]'))
    if sexo in 'MF':
        flag = 1
    else:
        print('Tente novamente')
print('-'*40)
flag = 0
while flag == 0:
    estado = str(input('Indique qual estado civil você se encontra[S/C/V/D]'))
    if estado in 'SCVD':
        flag = 1
    else:
        print('Tente novamente')
print('Cadastro realizado com sucesso')
