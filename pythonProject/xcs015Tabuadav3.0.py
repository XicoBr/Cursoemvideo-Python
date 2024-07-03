print('==' * 8, 'Tabuada v3.0', '==' * 8)
num = int(input('Quero ver a tabuada de [(-1) encerra]: '))
while num != -1:
    for cont in range(1, 11):
        print(f'{num} x {cont} =', num * cont)
        cont += 1
    num = int(input('Digite outro valor para a tabuada [(-1) encerra]: '))
    print('=-=' * 20)
print('Program ENCERRADO!')
