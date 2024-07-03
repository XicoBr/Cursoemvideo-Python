from random import randint
from time import sleep
resutados = dict()  # dicionario {}
jogadores = list()  # lista []    tupla ()
print('Valores sorteados:')
for c in range(0, 4):  # c= contador qualquer
    n = randint(1, 6)  # n= recebe um valor aleatório entre 1 e 6
    resutados['Jogador ' + str(c + 1)] = n  # adiciona o jogador com o valor do dado ao dicionário resultados
    jogadores.append(n)  # adiciona o valor do dado à lista jogadores
    sleep(0.9)
    print(f'O {"Jogador " + str(c + 1)} tirou {n}')
jogadores.sort(reverse=True)  # inverte a ordem da lista jogadores
jogar = 't'
print('-=' * 15)
print('Ranking dos jogadores:')
for p in range(0, 4):
    print(f'{p + 1}º Lugar: ', end='')
    for k, v in resutados.items():
        if v == jogadores[p] and jogar != k:
            sleep(0.1)
            print(k, 'com', v)
            jogar = k  # usa-se o break e o jogar = k para evitar que o resultado 'quebre', já que se não tiver o
            # break, ele repete o resultado
            break
