print('=-=' * 20)
print(f'{'É TRIÂNGULO OU É TABASCO?':>40}')
print('=-=' * 20)
r1 = float(input('Digite o valor da R1: '))
r2 = float(input('Digite o valor da R2: '))
r3 = float(input('Digite o valor da R3: '))
ref = r1
print('=-=' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo formado é equilátero, pois tem todos os lados iguais')
    elif r1 == r2 or r1 == r3:
        print('O triângulo é isósceles, pois tem 2 lados iguais')
    if r1 != r2 != r3 != r1:
        print('O triangulo formado é escaleno, pois todos os lados são diferentes')
else:
    print('Não pode formar triângulo')