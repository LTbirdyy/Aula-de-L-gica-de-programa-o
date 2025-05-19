print('Fale até onde na sequéncia de Fibonacci você deseja que ele vá')
fibo = int(input('Até qual número da sequência:'))
n1 = 0
n2 = 1
n3 = n2 + n1
print('A sequência ficaria: 1', end=' ')
for c in range(0, fibo - 1):
    print(f'{n3}', end=' ')
    n1 = n2
    n2 = n3
    n3 = n2 + n1
