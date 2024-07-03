r1 = int(input('Digite a Reta 1: '))
r2 = int(input('Digite a Reta 2: '))
r3 = int(input('Digite a Reta 3: '))
if r2 + r3 > r1 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo')
