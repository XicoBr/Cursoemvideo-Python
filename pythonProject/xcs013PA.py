print('==' * 20)
print(f'{'10 TERMOS DE UMA PA':^40}')
print('==' * 20)
a1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = a1 + (10 - 1) * raz
cont = 0
for c in range(a1, decimo + raz, raz):
    print(c, end = " ==> ")
print('FIM')
