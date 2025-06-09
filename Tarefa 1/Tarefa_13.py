#DADOS
sexo = input('Qual é o seu sexo [M/F]').upper().strip()[0]
peso = int(input('Qual seu peso em KG:'))
altura = int(input('Qual sua altura em CM:'))
idade = int(input('Qual sua idade:'))
if sexo == 'M':
    TMB = 66.47 +(13.75 * peso) + (altura * 5.003) - (6.755 * idade)
if sexo == 'F':
    TMB = 655.09 +(9.563* peso) + (altura * 1.85) - (4.676 * idade)
print(f'A sua TMB sera {TMB}')
