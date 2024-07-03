valor = int(input('Digite um valor [0 a 9999]: '))
u = valor // 1 % 10 #o resto será a divisão de (valor) por 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000
print(f'A unidade de {valor} é {u}')
print(f'A dezena de {valor} é {d}')
print(f'A centena de {valor} é {c}')
print(f'O milhar de {valor} é {m}')
