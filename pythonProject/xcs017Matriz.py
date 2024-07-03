mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('-=' * 20)
print(f'{'MATRIZ 3x3':>25}')
print('-=' * 20)
for l in range(0, 3):  # primeiro range para leitura dos valores
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite o valor na posição [{l}] [{c}]: '))  # adiciona o valor na pos.[l][c]
print('=-=' * 20)
for l in range(0, 3):  # segundo range para mostrar os valores em tela
    for c in range(0, 3):
        print(f'[{mat[l][c]:^10}]', end='')
    print()  # quebra de linha, faz com que aja colunas
