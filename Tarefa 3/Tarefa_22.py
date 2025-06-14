# 22) Faça uma função chamada Matriz() que recebe dois números inteiros
# positivos (linhas e colunas) e um valor booleano e retorna uma matriz (lista
# de listas). Se o valor booleano for True, então a matriz deverá receber
# valores aleatórios entre -3 e 3. Se for False (valor default), deverá retornar
# uma matriz com todos os elementos iguais a zero.
from random import randint, sample


def matriz(linha, colunas, random=False):
    flag = 0
    while flag != linha * colunas:
        # Definindo o que vai dentro da matriz
        if random:
            # Escrevendo a matriz
            for l in range(0, linha):
                if l != 0:
                    print('')
                for c in range(0, colunas):
                    print(f'[{randint(-3, 3):2d}]', end='')
                    flag += 1
        else:
            elementos = 0
            # Escrevendo a matriz
            for l in range(0, linha):
                if l != 0:
                    print('')
                for c in range(0, colunas):
                    print(f'[{elementos}]', end='')
                    flag += 1


matriz(linha=int(input('Fale o número de linhas: ')),
       colunas=int(input('Fale o número de colunas: ')),
       random=bool(input('Deseja que a matriz tenha valores(Deixe em branco se não):')))
