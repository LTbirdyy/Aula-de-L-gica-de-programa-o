n1 = int(input('Fale o primeiro número'))
salvo1 = n1
n2 = int(input('Fale o segundo número'))
salvo2 = n2
# MDC
if n1 == n2:
    print(f'O MDC é {n1}')
elif n1 < n2:
    n1 = n2
    temp = n2
    n2 = n1
resto = n1 % n2
while resto != 0:
    n1 = n2
    n2 = resto
    resto = n1 % n2
# MMC
n1 = salvo1
n2 = salvo2
if n1 > n2:
    maior = n1
else:
    maior = n2

while True:
    if maior % n1 == 0 and maior % n2 == 0:
        mmc = maior
        break
    maior += 1

print(f'O MDC é {n2} e o MMC é {mmc}')
