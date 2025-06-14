def resolver_equacao(equacao):
    print(f"Equação original: {equacao}")
    print('-' * 20)

    # Remove espaços
    equacao = equacao.replace(' ', '')

    # Separa a equação em lados igual na questão anterior
    lado_esquerdo, lado_direito = equacao.split('=')

    # Identifica o termo com x (ax) e o termo constante (b)
    if 'x' not in lado_esquerdo:
        return "Formato inválido. A equação deve ter 'x' no lado esquerdo."

    # Encontra índice do 'x'
    pos_x = lado_esquerdo.find('x')

    # Coeficiente a
    termo_a = lado_esquerdo[:pos_x]
    if termo_a == '' or termo_a == '+':
        a = 1
    elif termo_a == '-':
        a = -1
    else:
        a = int(termo_a)

    # Constante b
    b_str = lado_esquerdo[pos_x + 1:]  # o que vem depois do x
    if b_str == '':
        b = 0
    else:
        b = int(b_str)

    c = int(lado_direito)

    # Etapa 1 – passar b para o outro lado
    if b < 0:                                 # Se b for negativo
        print(f'Etapa 1: {a}x = {c} + {-b}')
        c += -b
        print('-'*20)

    elif b > 0:                                # Se b for positivo
        print(f'Etapa 1: {a}x = {c} - {b}')
        c -= b
        print('-'*20)

    else:                                      # Se b for nulo
        print('-'*20)

    # Etapa 2 – resultado do lado direito
    print(f'Etapa 2: {a}x = {c}')
    print('-' * 20)

    # Etapa 3 – isolar x
    print(f'Etapa 3: x = {c}/{a}')
    print('-' * 20)

    # Etapa 4 – resultado final
    resultado = c / a
    print(f'Etapa 4: x = {resultado}')
    print('-' * 20)


resolver_equacao(equacao=input('Fale a equação: '))
