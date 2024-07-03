tupla = ()
cont9 = par = 0
c = 1
for c in range(1, 6):
    n = int(input(f'Digite o {c}º número: '))
    tupla += n,
    if n == 9:
        cont9 += 1
    if n % 2 == 0:
        par += 1
print(f'Números digitados: {tupla}')
print(f'Total de números pares: [{par}]')
if cont9 >= 1:
    print(f'Total de números 9: [{cont9}]')
if 3 in tupla:
    print(f'Primeiro 3 na posição [{tupla.index(3) + 1}]')