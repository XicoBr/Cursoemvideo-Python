from random import randint
from time import sleep
print(f'{"============= ADIVINHA O NÚMERO =============":^40}')
r = input('Quer começar? [s/n] ').lower()
pc = randint(0, 10)
content = 0  # quantas tentativas para acertar
while r == 's':
    print(f'Tentativas: {content}')
    num = int(input('Digite um número entre 0 e 10 para você tentar adivinhar: '))
    while num not in range(0, 11):
        print('Ei, esse número não tá valendo!')
        r = input('Quer digitar outro número? [s/n] ').lower()
        num = int(input('Digite um número entre 0 e 10 para você tentar adivinhar: '))
    print('=-=' * 20)
    print('Espera aí...')
    print('=-=' * 20)
    sleep(1.2)
    if num != pc:
        content += 1
        r = input(f'Rá! Você errou!\nQuer tentar de novo? [s/n] ').lower()
        if r == 'n':
            print(f'Só pra você saber, eu pensei no número {pc} e você digitou {num}.')
    if num == pc:
        print(f'Tentativas até acertar: {content}')
        r = input(f'Droga! Você acertou, pé de rato! Eu pensei no número {pc}.\nQuer jogar de novo? [s/n] ').lower()
        content = 0
        print('=-=' * 20)
print('Até mais, otário!')
