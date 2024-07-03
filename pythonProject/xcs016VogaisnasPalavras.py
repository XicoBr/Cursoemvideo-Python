# CONTADOR DE VOGAIS NAS PALAVRAS USANDO TUPLA
palavras = ()  # tupla sem valores, que serão adicionados posteriormente
vogais = ('A', 'E', 'I', 'O', 'U')  # tupla de vogais para verificação nas palavras
while True:
    pal = input('Digite a palavra para análise [sem acentos].\n[Digite 000 para encerrar]: ').upper().strip()
    print('=-=' * 10)
    if pal == '000':
        break
    palavras += pal,
for c in range(0, len(palavras), 1):  # c = contador; vai da pos. 0 até o comprimento da tupla PALAVRAS
    print('')
    print(f'A palavra {palavras[c]} tem as vogais', end=' ')
    for v in range(0, len(vogais)):  # v = contador de vogais; vai da pos. 0 até o comprimento da tupla VOGAIS
        if vogais[v] in palavras[c]:
            print(f'\033[33m{vogais[v]}\033[m', end=' ')
