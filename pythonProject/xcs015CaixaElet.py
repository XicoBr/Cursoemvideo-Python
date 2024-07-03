print('=-=' * 17)
print('{:^50}'.format('RABO BANK'))
print('=-=' * 17)
valor = int(input('Digite o valor para saque: R$ '))
# Método 1: Lógica Matemática
'''c50 = valor // 50 # aqui, dividimos o valor por 50, para sabermos quantas notas de 50 são necessárias
valor %= 50 # agora, setamos o valor para o resto da divisão por 50
c20 = valor // 20  
# dividimos o valor(que agora é resto de valor por 50) por 20 para vermos quantas notas de 20 são necessárias
valor %= 20 # setamos o valor para o resto de valor por 20
c10 = valor // 10
valor %= 10
c1 = valor // 1
print(f'Notas de R$ 50,00: {c50}')
print(f'Notas de R$ 20,00: {c20}')
print(f'Notas de 10,00: {c10}')
print(f'Notas de R$ 1,00: {c1}')'''

# Método 2: Uso de laços (DESAFIO 71)
total = valor  # total que  o caixa deve repassar ao cliente (exemplo usado: R$ 1.734,00)
ced = 50  # ponto de referencia. É a cédula de 50
totced = 0  # quantas cédulas de determinada nota são necessárias
while True:
    if total >= ced:  # ou seja, se 1734 maior que cedula atual, no caso 50 inicial:
        total -= ced  # vai diminuindo 50 reais do total, que é 1734
        totced += 1  # vai contando quantas cédulas são necessárias, no caso são 34 de R$ 50,00
    else:  # se o total for menor que a cedula:
        print(f'O total de cédulas de R$ {ced} é de {totced} ')
        # aqui ele mostra quantas cédulas de tal valor são necessarias
        if ced == 50:  # se o valor maior que 50, ele troca a ced por 20
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0  # zera sempre que um novo valor pra ced é chamado
        if total == 0:
            break
