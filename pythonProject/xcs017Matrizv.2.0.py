matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor na posição [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[l][c] == matriz[l][2]:
            soma3 += matriz[l][c]
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^10}]', end=' ')
    print()
print('-=' * 20)
print(f'Valores pares somados: {somapar}')
print(f'Valores da coluna 3 somados: {soma3}')
print(f'Maior valor da linha 2: {maior}')
