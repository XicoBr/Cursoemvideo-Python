from time import sleep
print('=-=' * 20)
print(f'{'BODEGA CACHAÇA E RAPARIGA':>41}')
print('=-=' * 20)
produto = float(input('Digite o preço do produto: R$ '))
print(f'{'FORMAS DE PAGAMENTO':>35}')
print('''
[1]: À vista no dinheiro(10% de desconto) 
[2]: À vista no cartão (5% de desconto)
[3]: 2x no cartão s/juros
[4]: 3x ou mais com 20% de juros ''')
print('=-=' * 20)
pagamento = str(input('Digite a forma de pagamento: '))
if pagamento == '1':
    print('Forma de pagamento: à vista no dinheiro')
    desc = produto - (produto * 0.1)
    print(f'Preço do produto com 10% de desconto: R$ {desc}')
    carteira = float(input('Digite o valor para pagamento: R$'))
    if carteira == desc:
        print('Processando...')
        sleep(2)
        print('Pagamento efetuado!')
    elif carteira > desc:
        print('Processando...')
        sleep(2)
        print('Pagamento efetuado!')
        print('Troco: R$', carteira - desc)
elif pagamento == '2':
    print('Forma de pagamento: à vista no cartão')
    desc = produto - (produto * 0.05)
    print(f'Preço do produto com 5% de desconto: R$ {desc}')
    carteira = float(input('Digite o valor para pagamento: R$ '))
    if carteira == desc:
        print('Processando...')
        sleep(2)
        print('Pagamento efetuado!')
    elif carteira > desc:
        print('Processando...')
        sleep(2)
        print('Pagamento efetuado!')
        print('Troco: R$', carteira - desc)
elif pagamento == '3':
    parc2 = produto / 2
    print('Forma de pagamento: parcelado 2 vezes s/juros')
    print('Valor para pagamento: R$ ', parc2)
    cont = input('Deseja continuar? [s]/[n] ')
    if cont == 's':
        print('Processando...')
        sleep(2)
        print('Pagamento efetuado!')
    elif cont == 'n':
        print('Operação cancelada!')
if pagamento == '4':
    print('Forma de pagamento: parcelado com juros')
    parc = int(input('Digite em quantas parcelas para pagamento: '))
    juros = ((produto / parc) * 1.2) + produto
    vparc = juros / parc
    print('Parcelas: ', parc)
    print('Valor final para pagamento: R$', juros)
    print('Valor de cada parcela: R$', vparc)
    cont = input('Deseja continuar? [s]/[n] ')
    if cont == 's':
        print('Processando...')
        sleep(2)
        print('Pagamento efetuado!')
    else:
        print('Operação cancelada!')
print('Tenha um excelente dia!')
