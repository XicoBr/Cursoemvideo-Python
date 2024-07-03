# funçao que lê nome e total de gols de um jogador no campeonato
# se nome vazio, colocar 'jogador desconhecido'
# se tot gols vazio, coloca "tot gols desconhecido"


def total_gols():
    """
    Teste de documentacao
    """
    nome_jogador = str(input('Digite o nome do jogador: '))
    if nome_jogador.strip() == '':
        nome_jogador = '<desconhecido>'
    tot_gols = str(input('Digite o número de gols: '))
    if tot_gols.isnumeric():
        tot_gols = int(tot_gols)
    else:
        tot_gols = 0
    return f'O jogador {nome_jogador} fez {tot_gols} gol(s)'


print(total_gols())
# help(total_gols)  # mostra a docstring da função
