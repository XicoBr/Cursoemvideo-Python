sal = int(input('Digite o salário: R$ '))
if sal > 1250:
    au = sal + (sal * 0.10)
    print(f'O novo salário com aumento será de: R$ {au}')
else:
    if sal <= 1250:
        aux = sal + (sal * (15/100))
        print(f'O novo salário com aumento será de: R$ {aux}')
