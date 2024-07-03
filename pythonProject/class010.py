"""tempo = int(input('Quantos anos o seu carro tem: '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')"""

#condição simplificada
"""tempo = int(input('Quantos anos tem seu carro? '))
print('Carro Novo' if tempo <= 3 else 'Carro Velho')
print('--FIM--')"""

n1 = float(input('Digite a Nota 1: '))
n2 = float(input('Digite a Nota 2: '))
n3 = float(input('Digite a Nota 3: '))
mnota = (n1 + n2 + n3) / 3
print(f'Média: {mnota:.1f}')
if mnota >= 7:
    print('Parabéns! Você passou de ano!')
else:
    print('Poxa, que pena! Você não passou de ano.')
print('------------------------------------------')
