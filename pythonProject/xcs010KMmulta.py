vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    acim = vel - 80
    mult = acim * 7
    print(f'MULTADO! Você está dirigindo a {vel} Km, excedendo o limite de 80 Km! ')
    print(f'A multa é de R$ {mult:.2f}. Cuidado na próxima vez.')
print('Tenha uma boa viagem! Dirija com segurança!')
print('=================FIM====================')