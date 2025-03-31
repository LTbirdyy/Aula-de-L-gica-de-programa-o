#TENTAR DNV
#ANIVERSÁRIO
dia = int(input('Fale o dia do seu aniversário'))
mes = int(input('Fale o mês do seu aniversário'))
mes = mes * 30
dia = mes - dia
#DATA ATUAL
dia_atual = 30
mes = 3 * 31
dia_atual = dia_atual - mes
if dia_atual < 0:
    resposta = dia + dia_atual
else:
    resposta = dia - dia_atual
if resposta < 0:
    print(f'Passaram {resposta*(-1)} do seu aniversário')
else:
    print(f'Faltam {resposta} para seu aniversário')
print(resposta)
print(dia)
print(dia_atual)