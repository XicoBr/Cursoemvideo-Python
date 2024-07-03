lista = ()
r = ''
while True:
    prod = input('Digite o nome do produto: ').upper()
    preco = float(input(f'Digite o preço do produto [{prod}]: R$ '))
    lista += prod, preco,  # CONFIG IMPORTANTÍSSIMA P/ ADICIONAR VALORES À TUPLA
    r = input('Deseja continuar?[s/n]').lower()
    while r != 'n' and r != 's':
        print('Opção inválida!')
        r = input('Quer continuar? [s/n]: ')
    if r == 'n':
        break
print('=-=' * 14)
print(f'{'TABELA DE PREÇOS':^40}')
print('=-=' * 14)
for pos in range(0, len(lista)):
    if pos % 2 == 0:  # Nome do produto
        print(f'{lista[pos]:.<30}', end='')

    else:  # Preço do produto
        print('R$', end='')
        print(f'{lista[pos]:>4.2f}')
print('=-=' * 14)
