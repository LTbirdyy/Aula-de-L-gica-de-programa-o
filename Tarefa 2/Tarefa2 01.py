soma = 0
cont = 0
while True:
    cont += 1
    n1 = int(input(f'Fale o {cont}º número para eu fazer a média dele:'))
    # SALVAR SOMA DOS NÚMEROS
    soma += n1
    # Terminar loop
    confirmar = int(input('Deseja adicionar outro número(caso não escreva um número negativo):'))
    if confirmar < 0:
        break
# CALCULO DA MÉDIA
media = soma/cont
print(f'A média é: {media}')
