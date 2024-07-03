# NÚMERO EM EXTENSO: DIGITAR UM NÚMERO COM ALGARISMOS E RETORNAR O VALOR POR EXTENSO

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete',
         'dezoito', 'dezenova', 'vinte')
r = ''
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num not in range(0, 21):
        print('Número Inválido! Tente novamente.')
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'O número que você digitou foi {tupla[num].upper()}')
    r = input('Quer continuar? [s/n]: ').lower()
    if r == 'n':
        break
print('PROGRAMA FINALIZADO!')
