from random import choice
from time import sleep
cores ={'limpatela':'\033[m', 'amarelo':'\033[33m', 'vermelho':'\033[31m', 'verde':'\033[32m'}
print(f'{" JOKENPÔ ":=^40}')
print('''                PLAYER
[1] Pedra     [2] Papel     [3] Tesoura''')
print('=' * 40)
usr = int(input('Escolha: '))
if usr == 1:
    usr = 'Pedra'
elif usr == 2:
    usr = 'Papel'
elif usr == 3:
    usr = 'Tesoura'
lista = ['Pedra', 'Papel', 'Tesoura']
pclista = choice(lista)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
print('=-=' * 20)
if usr == pclista:
    print(f'{cores['amarelo']}EMPATOU!{cores['limpatela']}')
    print('Player: ', usr)
    print('Computador: ', pclista)
elif (usr == 'Pedra' and pclista == 'Tesoura') or (usr == 'Papel' and pclista == 'Pedra') or (usr == 'Tesoura' and pclista == 'Papel'):
    print(f'Você {cores['verde']}GANHOU!{cores['limpatela']}')
    print('Player: ', usr)
    print('Computador: ', pclista)
elif (usr == 'Tesoura' and pclista == 'Pedra') or (usr == 'Pedra' and pclista == 'Papel') or (usr == 'Papel' and pclista == 'Tesoura'):
    print(f'Você {cores['vermelho']}PERDEU!{cores['limpatela']}')
    print('Player: ', usr)
    print('Computador: ', pclista)
