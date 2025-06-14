def extrair_coeficientes(equacao):
    # Remover espaços em branco
    equacao = equacao.replace(" ", "")

    # Separa os lados da equação
    lado_esquerdo, lado_direito = equacao.split('=')
    c = int(lado_direito)

    # Inicialização dos coeficientes
    a = 0
    b = 0

    # Encontra o índice do 'x'
    pos_x = lado_esquerdo.find('x')

    # Parte do coeficiente a
    parte_a = lado_esquerdo[:pos_x]
    if parte_a == '' or parte_a == '+':
        a = 1
    elif parte_a == '-':
        a = -1
    else:
        a = int(parte_a)

    # Parte depois do x é o b
    parte_b = lado_esquerdo[pos_x + 1:]
    if parte_b == '':
        b = 0
    elif parte_b[0] == '+':
        b = int(parte_b[1:])
    elif parte_b[0] == '-':
        b = -int(parte_b[1:])
    else:
        b = int(parte_b)

    return a, b, c


resposta = extrair_coeficientes(equacao='Fale a equação: ')
print(resposta)
