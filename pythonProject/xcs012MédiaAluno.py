from time import sleep
print('=-=' * 20)
print('LEITOR DE NOTA')
print('=-=' * 20)
n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
media = (n1 + n2) / 2
print('=-=' * 20)
print('AGUARDE...')
print('=-=' * 20)
sleep(2)
if media < 5:
    print('\033[31mREPROVADO\033[m')
    print(f'Média final: {media:.2f}pts')
elif media >= 5 and media <= 6.9:
    print(f'\033[33mRECUPERAÇÃO\033[m')
    print(f'Média final: {media:.2f}pts')
else:
    print('\033[32mAPROVADO')
    print(f'Média final: {media:.2f}pts')