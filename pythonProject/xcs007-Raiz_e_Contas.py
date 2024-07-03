import math

n = int(input('Digite um número: '))
n0 = n - 1
n2 = n + 1
dn= n * 2
tn = n * 3
rn = math.sqrt(n) #ou rn = n**1/2
rn1 = n**0.5
print(f'O antecessor de {n} é {n0}, e seu sucessor é {n2}')
print(f'Sua raiz é {rn:.0f}')


