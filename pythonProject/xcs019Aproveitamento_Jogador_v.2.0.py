continue_check = 'S'
jogador = dict()
lista_jogadores = list()
gols_partidas = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).upper().strip()
    partidas = int(input('Partidas disputadas: '))
    gols_partidas.clear()
    for i in range(0, partidas):
        gols_partidas.append(int(input(f'Gols na Partida {i + 1}: ')))
    jogador['gols'] = gols_partidas[:]
    jogador['gols_total'] = sum(gols_partidas)
    jogador['media_gols'] = sum(gols_partidas) / partidas if partidas > 0 else 0
    lista_jogadores.append(jogador.copy())

    while True:
        continue_check = str(input('Quer continuar? [s/n]: >> ')).upper()[0]
        if continue_check in 'SN':
            break
        print('Erro! Digite S ou N para continuar!')
    if continue_check in 'Nn':
        break

print('=' * 90)
print(f'{"cód":^7}', end='')
for i in jogador.keys():
    print(f'{i:^20}', end='')
print()
print('=' * 90)
for k, v in enumerate(lista_jogadores):
    print(f'{k:^7}', end='')
    for d in v.values():
        print(f'{str(d):^20}', end='')
    print()
print()
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 p/ cancelar]: > '))
    print('=' * 80)
    if busca == 999:
        break
    elif busca >= len(lista_jogadores):
        print('Erro! Tente novamente')
    else:
        print(f'-- Levantamento do Jogador {lista_jogadores[busca]['nome']}')
        for i, g in enumerate(lista_jogadores[busca]['gols']):
            print(f'  > Na Partida {i + 1}, fez {g} gol(s).')
        print(f'  > Média de gols: {lista_jogadores[busca]['media_gols']:.2f} gols / jogo')
    print('=' * 80)
print('Programa Encerrado!')
