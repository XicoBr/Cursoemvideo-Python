from time import sleep


def contador():
    print('--Contagem de 1 a 10')
    contador = 1
    print(' >  ', end='')
    while contador <= 10:
        sleep(0.5)
        print(f'{contador}', end='')
        if contador < 10:
            print('...', end='')
        contador += 1
    sleep(0.5)
    print()
    sleep(0.5)
    print('-=' * 24)
    print('--Contagem de 10 a 0')
    contador = 10
    print(' >  ', end='')
    while contador >= 0:
        sleep(0.5)
        print(f'{contador}', end='')
        if contador > 0:
            print('...', end='')
        contador -= 1
    sleep(0.5)
    print()
    print('-=' * 24)
    print('--Contagem personalizada')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo == 0:
        passo = 1
    sleep(1.0)
    print(f'Contagem de {inicio} a {fim}, de {abs(passo)} em {abs(passo)}')
    contador = inicio
    if inicio < fim:
        while contador <= fim:
            sleep(0.5)
            print(contador, end='')
            if contador != fim:
                print('...', end='')
            contador += passo
        print('  Fim!')
    else:  # inicio > fim
        while contador >= fim:
            sleep(0.5)
            print(contador, end='')
            if contador != fim:
                print('...', end='')
            contador -= passo
        print('  Fim!')


contador()
