# PROGRAMA 'LER E SOMAR' UTILIZANDO O BREAK
s = cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    s += num
    cont += 1
print('Encerrado')
print(f'Soma: {s}')
print(f'Números totais digitados: {cont}')
