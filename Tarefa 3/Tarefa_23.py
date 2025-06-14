def mostrar_matriz(matriz):
    for linha in matriz:            # Pega a quantidade de lista dentro da matriz
        for elementos in linha:     # Pega os lementos dentro da lista agr
            print(f'{elementos:3d}', end=' ')
        print()


matriz_feia = [
    [2, 3, 4],
    [5, 6, 7]
]

mostrar_matriz(matriz=matriz_feia)
