from random import randint, sample
'''cont = min = max = 0
print(f'Os números sorteados foram: ', end='')
while cont < 5:
    alet = (randint(0, 20))
    print(alet, end=' ')
    if cont == 0:
        max = alet
        min = alet
    else:
        if alet > max:
            max = alet
        if alet < min:
            min = alet
    cont += 1
print('')
print(f'O maior número foi: {max}')
print(f'O menor número foi: {min}')'''

#    2º MÉTODO:

'''a = tuple(sample(range(7), 6))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')'''
# sample é um looping; tuple encapsula os comandos que o sucedem

#  3º   MÉTODO ESCALÁVEL(PODE REPETIR VALORES, DIFERENTE DAS OPÇÕES ANTERIORES, TALVEZ A MELHOR SOLUÇÃO):
tupla = ()
for c in range(5):
    n = randint(1, 20)
    tupla += n,
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
