# MENU DE OPERAÇÕES COM 2 VALORES
from time import sleep
n1 = 0
n2 = 0
r = False
n1 = int(input('Digite o N1: '))
n2 = int(input('Digite o N2: '))
while not r:  # enquanto o 'r' não for Verdadeiro:
    print('=-=' * 20)
    print(f'             N1:', n1, '{:>25}'.format('N2:'), n2)
    print('=-=' * 20)
    print('Selecione a opção:')
    print(f'[1] Somar', '{:>33}'.format('[2] Multiplicar'))
    print(f'[3] Comparação', '{:>30}'.format('[4] Nova operação'))
    print('[5] Sair do programa')
    print('=-=' * 20)
    r = input('Opção escolhida: ')
    if r == '1':
        soma = n1 + n2
        print('Somando...')
        sleep(1)
        print(f'{n1} + {n2} = {soma}')
        r = input('Quer realizar outra operação? [s/n]: ')
        if r == 's':
            r = False
        else:
            r = True
    elif r == '2':
        mult = n1 * n2
        print('Multiplicando...')
        sleep(1)
        print(f'{n1} * {n2} = {mult}')
        r = input('Quer realizar outra operação? [s/n]: ')
        if r == 's':
            r = False
        else:
            r = True
    elif r == '3':
        lista = (n1, n2)
        print('Comparando...')
        sleep(1)
        print(f'O maior número é {max(lista)}')
        print(f'O menor número é {min(lista)}')
        r = input('Quer realizar outra operação? [s/n]: ')
        if r == 's':
            r = False
        else:
            r = True
    elif r == '4':
        r = False
        n1 = int(input('Digite o N1: '))
        n2 = int(input('Digite o N2: '))
    elif r == '5':
        r = True
        print('Encerrando', end='')
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
    else:
        print('Opção Inválida!')
        r = input('Quer tentar novamente?[s/n]: ')
        if r == 's':
            r = False
        else:
            r = True
print('=-=' * 20)
print('Operação Encerrada!')
