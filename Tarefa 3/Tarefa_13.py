texto = input('Escreva algum texto ou frase: ').lower()   # lower() evitar risco de vim exemplo 'GABRIEL' e quebrar tudo

# Separando as palavras com o split()
texto = texto.split(' ')

# Separando as letras dessas palavras
lista_letras = [list(palavra) for palavra in texto]   # o list(palavra) separa as letras dessa palavra

# Limpar lista original para receber o texto modificado
texto = []
letras = ''
for letras in lista_letras:
    letras[0] = letras[0].upper()       # Colocando em maiúsculo primeira
    letras[-1] = letras[-1].upper()     # E última letras

# Juntando letras modificadas

palavra_modificada = [''.join(letras) for letras in lista_letras]
texto = ' '.join(palavra_modificada)

print(texto)
