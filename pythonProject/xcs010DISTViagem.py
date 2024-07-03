dis = int(input('Digite a distância da viagem [km]: '))
if dis <= 200:
    pass2 = dis * 0.5
    print(f'O valor da passagem é: R${pass2:.2f}')
else:
    pass3 = dis * 0.45
    print(f'O valor da passagem é: R${pass3:.2f}')
