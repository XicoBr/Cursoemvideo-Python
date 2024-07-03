def ficha(jog='<desconhecido>', gol=0):
    return f'O jogador {jog} fez {gol} gol(s).'


# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0  # caso digite uma letra, a variavel g recebe 0 como valor
if n.strip() == '':
    print(ficha(gol=g))
else:
    print(ficha(n, g))
