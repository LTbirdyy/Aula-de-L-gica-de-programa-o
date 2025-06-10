# Fazendo com duas listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_rotacionada = []

ultimo_valor = lista[-1]                  # Salvando o ultimo valor da lista para poder jogar ele no inicio da nova
lista.pop(-1)                             # Eliminando o ultimo valor por se tornar repetido
lista_rotacionada.append(ultimo_valor)

for index in range(0, len(lista)):        # Adicionando os valores da 1ª lista na 2ª lista
    lista_rotacionada.append(lista[index])

print(f'Fazendo com duas listas {lista_rotacionada}')

# Fazendo com apenas uma lista
lista = [1, 2, 3, 4]
ultimo_valor = lista[-1]
lista.pop(-1)
lista.insert(0, ultimo_valor)
print(lista)




