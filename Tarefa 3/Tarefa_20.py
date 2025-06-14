def formar_triangulo(a, b, c):
    # Verificar se é possivel
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def perimetro_area(a=0, b=0, c=0):
    # Perimetro
    perimetro = a + b + c

    # Descobrindo a base
    maior_valor = a
    for i in range(0, 3):
        if maior_valor < b:
            maior_valor = b
        if maior_valor < c:
            maior_valor = c

    # Variável nomeada base para facilitar
    base = maior_valor

    # Descobrir a área usando fórmula de Heron

    semiperi = perimetro/2

    area = (semiperi*(semiperi-a)*(semiperi-b)*(semiperi-c))**0.5

    altura = (2 * area)/base

    return f'A área é {area:.2f} e o perimetro é {perimetro}'


valor_a = int(input('Fale o 1ª valor: '))
valor_b = int(input('Fale o 2ª valor: '))
valor_c = int(input('Fale o 3ª valor: '))


resposta_triangulo = formar_triangulo(a=valor_a,
                                      b=valor_b,
                                      c=valor_c)
if resposta_triangulo:
    resposta_area_2p = perimetro_area(a=valor_a,
                                      b=valor_b,        # Utiliza os mesmos valores dados anteriormente
                                      c=valor_c)
    print(resposta_area_2p)
else:
    print('Por não ser triângulo não pode fazer a outra operação')
