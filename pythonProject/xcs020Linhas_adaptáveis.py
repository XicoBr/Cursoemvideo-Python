# escrever uma função que faça com que as linhas visuais acompanhem o tamanho da string, centralizando o texto


def linhas(texto):
    tamanho = len(texto) + 4
    print('-' * tamanho)
    print(texto.center(tamanho))
    print('-' * tamanho)


linhas('CeV')
