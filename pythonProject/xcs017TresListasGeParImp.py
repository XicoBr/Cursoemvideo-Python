#  CRIAR 3 LISTAS: GERAL, PAR E IMPAR
# NO FINAL MOSTRAR CADA UMA DELAS
geral = []
par = []
impar = []
while True:
    n = int(input('Digite um número [000 p/ encerrar]: '))
    if n == 000:
        break
    geral.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'Lista geral: {geral}')
print(f'Lista Nº PARES: {par}')
print(f'Lista Nº ÍMPARES: {impar}')
