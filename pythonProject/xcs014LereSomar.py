soma = num = cont = 0
num = int(input('Digite um número [999 para parar]: ')) # coloca o num fora do laço, para que  o 999 nao seja contabilizado
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: ')) # coloca o num no final do while, para que o 999 não seja contabilizado
print(f'Números digitados: {cont}')
print(f'A soma foi de: {soma}')
print('Programa encerrado')
