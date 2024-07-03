from math import pow, sqrt, hypot
'''co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hip = sqrt(pow(co, 2) + pow(ca, 2))
print(f'A hipotenusa vale {hip:.0f}')'''

'''ou poderia ser'''''
from math import hypot
co = int(input('Digite o CO: '))
ca = int(input('Digite o CA: '))
hip = hypot(co,ca)
print('A hipotenusa é', hip)

'''ou
co = float(input('Digite o CO: ')
ca = float(input('Digite o CA: ')
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vale ', hip)'''