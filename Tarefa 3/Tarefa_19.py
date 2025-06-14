def formar_triangulo(a, b, c):
    # Verificar se é possivel
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


resposta = formar_triangulo(a=int(input('Fale o 1ª valor: ')),
                            b=int(input('Fale o 2ª valor: ')),
                            c=int(input('Fale o 3ª valor: ')))
print(resposta)
