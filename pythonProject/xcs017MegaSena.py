from random import randint
from time import sleep
name = "MEGA SENA"
lista = []
jogos = []
c = 0
cont = 0
print(name.center(50, '='))
bet = int(input('Digite a quantia de jogos para gerar: '))
while cont <= bet:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
    if len(lista) == 6:
        lista.sort()
        jogos.append(lista[:])
        cont += 1
        lista.clear()
    if cont == bet:
        break
print(f'NÚMERO DE JOGOS: {bet}')
sleep(1)
print('POR FAVOR... AGUARDE...')
sleep(2)
for i, l in enumerate(jogos):  # para cada indice com a lista
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('BOA SORTE!')