"""Programa que leia 7 valores numéricos e coloque-os em LISTA ÚNICA
- quantos pares;
- quantos ímpares;
- no final, mostrá-los em ordem crescente"""

geral = [[], []]  # listas dentro de uma lista, pos.0= par; pos.1= ímpar
for cont in range(1, 8):
    num = int(input(f'Digite o {cont}º valor: '))
    if num % 2 == 0:
        geral[0].append(num)  # adiciona o NUM na POS.0 de GERAL(PAR)
    else:
        geral[1].append(num)
geral[0].sort()  # coloca os num. pares em ordem crescente
geral[1].sort()  # coloca os num. impares em ordem crescente
print('=-=' * 20)
print(f'Números pares: {geral[0]}')
print(f'Números ímpares: {geral[1]}')
