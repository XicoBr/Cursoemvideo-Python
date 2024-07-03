from random import randint
from time import sleep #faz o pc dormir por alguns segundos
numrd = randint(0, 5) #Faz o Pc ''pensar''
usr = int(input('Digite um número [0 a 5] para tentar adivinhar qual o PC escolheu: '))
print('-=-' * 20)
print('    Aguarde...Processando...')
print("-=-" *20)
sleep(2)
if usr == numrd:
    print('  Parabéns! Você acertou!')
else:
    print(f'  Você errou! Eu escolhi {numrd}. Tente  de novo.')
