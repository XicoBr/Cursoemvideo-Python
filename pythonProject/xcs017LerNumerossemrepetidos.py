lista = []
numero = 0
r = ''
while True:
    print('=-=' * 20)
    numero = int(input('Digite um número [digite 000 para encerrar]: '))
    if numero == 000:
        break
    if numero in lista:
        print('=-=' * 20)
        print(f'Erro! Número {numero} já registrado!')

    elif numero not in lista:
        lista += numero,
lista.sort()
print(f'Os números em ordem crescente são: {lista}')

