# Leitor de Expressão Matemática
# Validador de expressões

# MÉTODO 1: USANDO IF
'''expr = str(input('Digite a expressão: '))
pilha = list()  # outra maneira de fazer uma lista
parabre = parfec = 0
for simb in expr:
    if simb == '(':
        parabre += 1
    elif simb == ')':
        parfec += 1
if parabre == parfec:
    print('Expressão Válida')
else:
    print('Expressão inválida')'''

# MÉTODO 2: GUANABARA
expr = str(input('Digite a expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()  # remove o parent. aberto da lista
        else:
            pilha.append(')')  # sinal de que teve mais parenteses fechando que abrindo
            break
if len(pilha) == 0:  # significa que a quant. de parent. abertos e fechados é igual
    print('Expressão Válida.')
else:
    print('Expressão Inválida!')