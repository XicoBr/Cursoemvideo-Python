from time import sleep
import os

print('=-=' * 20)
print(f'{'LEITOR DE IMC':>35}')
print('=-=' * 20)
#nome = input('Digite o seu nome: ')
#idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura [cm]: '))
altcm = altura / 100
peso = float(input(f'Digite o seu peso [kg]: '))
imc = peso / (altcm ** 2)
y = (18.5 * (altcm ** 2)) - peso
x = - (25*(altcm ** 2)) + peso
print(f'IMC: {imc:.1f}')
if imc < 18.5:
    print('Está abaixo do peso ideal.')
    print(f'Você precisa ganhar pelo menos {y:.2f} kg para voltar para o peso ideal.')
elif 18.5 <= imc < 25:
    print('\033[32mPARÁBENS!\033[m')
    print('Você está dentro do peso ideal!')
elif 25 <= imc < 30:
    print('Está acima do peso ideal.')
    print(f'Você precisa perder pelo menos {x:.2f} kg para voltar para o peso ideal.')
elif 30 <= imc < 40:
    print('Está na faixa de obesidade.')
    print(f'Você precisa perder pelo menos {x:.2f} kg para voltar para o peso ideal.')
if imc >= 40:
    print('Está na faixa de obesidade mórbida')
    print(f'Você precisa perder pelo menos {x} kg para voltar para o peso ideal.')
