import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O seno de {ang} é {seno:.2f}')
print(f'O cosseno de {ang} é {coss:.2f}')
print(f'O tangente de {ang} é {tang:.2f}')