# JOGO DE DADOS

from random import randint
from time import sleep
pos = 1
jogador = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(
    1, 6)
           }
for j, v in jogador.items():
    print(f'{j} tirou [{v}]')
    sleep(1)
print('')
print('=-=' * 3, 'Ranking de Jogadores', '=-=' * 3)
ranking = dict(sorted(jogador.items(), key=lambda item: item[1], reverse=True))
# O `key=lambda item: item[1]' faz com o sort seja feito a partir dos valores que os jogadores obtiveram.
# Se quiser fazer com as chaves ao invés dos valores, use item[0]. Assim não precisar importar e fazer uso do itemgetter
for j, v in ranking.items():
    print(f'{pos}o. lugar: {j} tirou [{v}]')
    pos += 1
    sleep(1)
