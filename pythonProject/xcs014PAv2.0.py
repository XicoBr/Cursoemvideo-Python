print('=-=' * 15)
print(f'{'PA DE 10 TERMOS v2.0':^45}')
print('=-=' * 15)
primeiro = int(input('Início da PA: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
print(primeiro, end=' -> ')
while cont < 10:
    termo += razao
    print(termo, end='')
    print(' -> ' if cont < 9 else '', end='')
    cont += 1
