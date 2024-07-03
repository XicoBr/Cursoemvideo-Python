# criar uma função que receba 3 paramêtros: inicio, fim, passo
# mostrar primeiro 1 a 10, passo 1
# mostrar segundo 10 a 0, passo 2
# mostrar terceiro contagem personalizada pelo usuário
from time import sleep


def contador():

    cont = 1
    print('-=' * 15)
    print('Contagem de 1 a 10, de 1 em 1')
    while cont <= 10:
        sleep(0.5)
        print(cont, end=' ')
        cont += 1

    print()
    sleep(0.5)
    cont = 10
    print('-=' * 15)
    print('Contagem de 10 a 0, de 1 em 1')
    while cont >= 0:
        sleep(0.5)
        print(cont, end=' ')
        cont -= 1

    print()
    print('-=' * 15)
    print('Contagem personalizada')
    print('-=' * 15)
    sleep(0.6)
    inicio = int(input('Digite o ínicio: '))
    fim = int(input('Digite o fim: '))
    passo = int(input('Digite o passo: '))
    if inicio < fim and passo == 0:
        passo = 1
    elif inicio > fim and passo == 0:
        passo = -1

    index = inicio

    if inicio < fim:
        while index <= fim:
            sleep(0.5)
            print(index, end='')
            if index < fim:
                print('..', end='')
            resultado = index + passo
            index = resultado

    elif inicio > fim:
        while index >= fim:
            if passo < 0:
                sleep(0.6)
                print(index, end='')
                if index > fim:
                    print('...', end='')

                resultado = index + passo
                index = resultado
            elif passo > 0:
                sleep(0.6)
                print(index, end='')
                if index > fim:
                    print('...', end='')
                resultado = index - passo
                index = resultado
    print()
    print('Programa encerrado!')


contador()
