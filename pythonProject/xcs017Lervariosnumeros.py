# Ler numero em lista
# Quantos numeros digitados
# Lista em ordem DECRESCENTE
# Se o valor 5 foi digitado e está ou não na lista
r = ''
decresc = []
digi = pos = 0
while True:
    decresc.append(int(input('Digite um valor: ')))
    digi += 1
    r = input('Quer continuar? [s/n]: ').lower()
    while r != 's' and r != 'n':
        print('Erro!')
        r = input('Quer continuar?[s/n]').lower()
    if r == 'n':
        break
decresc.sort(reverse=True)
print('=-=' * 20)
print(f'Elementos digitados: {digi}')
print(f'A lista em ordem decrescente é: {decresc}')
if 5 in decresc:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não faz parte da lista.')
