# criar duas funções
# a primeira cria uma lista com 5 números aleatórios
# a segunda função mostra a soma de todos os números pares
from random import randint
from time import sleep


def numeros():
    lista_numeros = list()
    for i in range(0, 5):
        lista_numeros.append(randint(1, 10))
    print('Sorteando os valores: ', end='')
    sleep(0.8)
    for valores in lista_numeros:
        print(f'|{valores}', end='| ')
        sleep(0.8)
    print()
    sleep(0.8)

    def soma_par():
        par_soma = 0
        for numero in lista_numeros:
            if numero % 2 == 0:
                par_soma += numero
        print(f'Soma dos valores pares é igual a {par_soma}')

    soma_par()


numeros()
