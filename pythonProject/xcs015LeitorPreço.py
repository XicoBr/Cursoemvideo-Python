preco = Mmil = mbarato = soma = 0
nmbarato = r = ''
cont = 1
while True:
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preço do produto: R$ '))
    if preco >= 1000:
        Mmil += 1
    if cont == 1:
        mbarato = preco
        nmbarato = nome
    else:
        if preco < mbarato:
            mbarato = preco
            nmbarato = nome
    cont += 1
    soma += preco
    r = input('Quer continuar? [s/n]: ').lower()
    while r != 's' and r != 'n':
        r = input('Opção inválida! Quer continuar? [s/n]: ').lower()
    if r == 'n':
        break
print(f'Valor total: R$ {soma}')
print(f'Total de produtos acima de R$ 1.000: {Mmil}')
print(f'O produto mais barato: {nmbarato.upper()} no valor de R$ {mbarato}')
