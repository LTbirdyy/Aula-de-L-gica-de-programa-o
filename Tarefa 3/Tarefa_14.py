texto = input('Fale algum texto ou frase: ')

lista = [len(tamanho) for tamanho in texto.split()]    # O .split() separa os valores guardados em "texto"
                                                                 # O len(tamanho) conta o tamanho dos textos
print(texto)
print(lista)
