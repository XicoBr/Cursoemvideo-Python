'''lista = []  # lista vazia que será preenchida com o peso das idade
for p in range(1, 4): # p = idade
    peso = float(input(f'P{p} - Digite o peso: '))
    lista += [peso]
print('O maior valor é', max(lista))
print('O menor valor é', min(lista))'''

# Método 2:
maior = 0
menor = 0
for p in range(1, 4):
    peso = float(input(f'P{p} - Digite o peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg')
print(f'O menor peso é {menor}kg')







