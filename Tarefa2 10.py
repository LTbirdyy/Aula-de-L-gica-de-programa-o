numero = int(input('Fale algum número e direi se é primo:'))
if numero == 2 or numero == 3 or numero == 5 or numero == 7:
    print('É primo')
elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
    print('Não é primo')
else:
    print('É primo')