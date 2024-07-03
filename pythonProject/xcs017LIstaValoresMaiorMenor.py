valores = []
pos = maior = menor = 0
for cont in range(1, 6):
    valores.append(int(input(f'Digite o {cont}º valor: ')))
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'Maior valor: {v} na posição: {pos}')
    elif v == min(valores):
        print(f'Menor valor: {v} na posição: {pos}')
