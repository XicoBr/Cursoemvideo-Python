from random import randint
print('==' * 20)
print(f'{'JOGO DO PAR OU ÍMPAR':^40}')
print('==' * 20)
cont = soma = 0
print('VAMOS COMEÇAR!')
while True:
    print('=-=' * 20)
    print(f'Vitórias consecutivas: {cont}')
    usr = int(input('Digite um valor: '))
    usrdec = input('Escolha entre par ou ímpar [P/I]: ').lower()
    pc = randint(0, 10)
    soma = usr + pc
    if usrdec == 'p':
        if soma % 2 == 0:
            print(f'{usr} + {pc} = {soma}')
            print('Deu PAR! Você ganhou!')
            cont += 1
        else:
            print(f'{usr} + {pc} = {soma}')
            print('Você perdeu!')
            break
    else:
        if soma % 2 == 1:
            print(f'{usr} + {pc} = {soma}')
            print('Você GANHOU!')
            cont += 1
        else:
            print(f'{usr} + {pc} = {soma}')
            print('Você perdeu!')
            break
print('Obrigado por jogar!')