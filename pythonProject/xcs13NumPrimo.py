num = int(input('Digite um número: '))
cores = {'limpa':'\033[m', 'verde':'\033[32m'}
contdiv = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=" ")
        contdiv += 1
    else:
        print('\033[m', end=" ")
    print(c, end=" ")
if contdiv > 2:
    print('\n\033[mNão é primo')
    print(f'O número {num} é divisível por {contdiv} números diferentes')
elif contdiv == 2:
    print('\n\033[mÉ primo')
