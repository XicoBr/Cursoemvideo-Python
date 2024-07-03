r = '1'
menv = soma = cont = maiv = media = 0
while r == '1':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        menv = maiv = num
    else:
        if num > maiv:
            maiv = num
        elif num < menv:
            menv = num
    r = input('Quer adicionar outro valor? [1S/2N]: ')
media = soma / cont
print(f'A média foi de: {media:.1f}')
print(f'A soma foi de: {soma}')
print(f'O maior valor foi de: {maiv}')
print(f'O menor valor foi de: {menv}')
