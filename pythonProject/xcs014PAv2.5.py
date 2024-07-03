print('=-=' * 15)
print(f'{'SUPER PA v2.5':^44}')
print('=-=' * 15)
primeiro = int(input('Digite o A1: '))
razao = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
print(primeiro, end=' -> ')
an = 1
r = ''
while cont < 10:
    termo += razao
    print(termo, end='')
    print(' -> ' if cont < 9 else '', end='')
    cont += 1
    an += 1
print('')
r = int(input('Quer mostrar mais quantos termos? '))
while r != 0:
    cont = 1
    while cont < r + 1:
        termo += razao
        print(termo, end='')
        print(' -> ' if cont < r else '', end='')
        cont += 1
        an += 1
    print('')
    r = int(input('Quer mostrar mais quantos termos? '))
print(f'Foram mostrados {an} termos')