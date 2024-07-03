somap = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        somap += num
if somap % 2 == 0:
    print(f'A soma dos pares foi igual a {somap}')
