def formar_triangulo(a, b, c):
    # Verificar se é possivel
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def perimetro_area(a, b, c):
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

    altura = (2 * area) / base

    return area, perimetro


def altura_relativa(area, a, b, c):
    altura_a = (2*area) / a
    altura_b = (2*area) / b
    altura_c = (2*area) / c
    # Usar a função sorted para organizar
    lista_temp = [float(f'{altura_a:.2f}'), float(f'{altura_b:.2f}'), float(f'{altura_c:.2f}')]
    lista_asc = sorted(lista_temp)

    return lista_asc


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
    # Respondendo de forma bonita
    for i in range(0, 2):
        if i == 0:
            print(f'Area: {resposta_area_2p[0]:.2f}')
        else:
            print(f'Perimetro: {resposta_area_2p[1]}')

    resposta_altura = altura_relativa(area=resposta_area_2p[0],
                                      a=valor_a,
                                      b=valor_b,
                                      c=valor_c)
    # Respondendo de forma bonita
    print('As três alturas aproximadas em ordem crescente:')
    print(*resposta_altura, sep=', ')

else:
    print('Por não ser triângulo não pode fazer a outra operação')
