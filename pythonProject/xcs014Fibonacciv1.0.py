print(f'======== Sequência de Fibonacciv 1.0 =========')
r = 's'
while r == 's':
    termo = int(input('Digite o número de termos da sequência: '))
    n0 = 0
    n1 = 1
    cont = 3
    print('0 -> 1 -> ', end='')
    while cont <= termo:
        fib = n0 + n1
        print(fib, ' -> ' if cont < termo else '', end='')
        cont += 1
        n0 = n1
        n1 = fib
    print('')
    r = input('Quer continuar? [s/n]: ').lower()
print('Encerrado')
