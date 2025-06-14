def equa(a, b, c):

    # Sinal que acompanha A caso seja 1
    if abs(a) == 1:
        if a > 0:
            a = '+x'       # Sinal positivo
        else:
            a = '-x'       # Sinal negativo

    # Qualquer outro valor para A
    elif abs(a) != 1 and a != 0:
        a = str(a) + 'x'

    # Caso A == 0
    else:
        return 'Valor inválido para A, tente novamente.'

    # sinal que acomapanha B
    if b == 0:
        return f'{a} = {c}'  # Já da return aqui caso não tenha b para evitar as demais etapas
    elif b > 0:
        b = '+' + str(b)    # Concatenando o valor de b com o sinal
    else:
        b = '-' + str(abs(b))  # abs() para não ficar repetido o sinal

    # Parte de escrever as expressões
    return f'{a} {b} = {c}'


# Coloquei tratament de erro para caso alguem não coloque nenhum valor nas opções

try:
    resposta = equa(a=float(input('Fale o valor de A(Diferente de 0): ')),
                    b=float(input('Fale o valor de B: ')),
                    c=float(input('Fale o valor de c: ')))

    print(resposta)

except ValueError:
    print('Não deixe valores em branco caso seja 0 coloque 0.')

