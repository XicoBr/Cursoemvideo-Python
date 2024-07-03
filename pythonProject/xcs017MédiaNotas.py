"""Programa que leia:
- NOMES;
- NOTAS;
- MÉDIAS de alunos em uma LISTA COMPOSTA"""
from time import sleep
geral = []  # ou geral = list()
r = ''
cont = 1
# lista = [nome, [nota1, nota2], media]
while True:
    nota1 = nota2 = 0
    nome = str(input(f'Nome aluno(a) [{cont}]: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], media])
    r = input('Quer continuar? [s/n]: ').lower()
    if r == 'n':
        break
    cont += 1
print('=-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(geral):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Quer ver as notas de qual aluno(a)? [999 finaliza]: '))
    if opc == 999:
        print('=-=' * 20)
        print('Finalizando...')
        sleep(1)
        break
    if opc <= len(geral) - 1:
        print('=-=' * 20)
        print(f'As notas de {geral[opc][0]} são {geral[opc][1]}')
