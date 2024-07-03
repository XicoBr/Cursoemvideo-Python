# APROVEITAMENTO DE JOGADOR
# ler nome, numero de partidas disputadas, número de gols
# retornar as informações acima de forma organizada, total de gols marcados e quantos gols marcados em cada partida

jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = dict()
jogador['partidas'] = int(input('Partidas disputadas: '))

for i in range(jogador['partidas']):
    partidas[f'jogo {i + 1}'] = int(input(f'Partida {i + 1}: '))

print('-=' * 15)
print(f'Nome do jogador: {jogador['nome']}')
print(f'Partidas disputadas: {jogador['partidas']}')

for k, v in enumerate(partidas.values()):
    print(f'> Gols na Partida {k + 1}: ', end='')
    if v == 1:
        print(f'1 gol.')
    elif v == 0:
        print(f'não marcou.')
    else:
        print(f'{v} gols.')

gols_total = sum(partidas.values())
gols_media = gols_total / jogador['partidas']
print(f'> Total de gols marcados: {gols_total} gols.')
print(f'> Média de gols: {gols_media:.2f} gol(s) / jogo')
