"""lista que mostre:
 - numeros de idade cadastradas;
 - idade mais pesadas (use um limitador);
 - idade abaixo do limitador."""

"""geral = list()  # info geral
dado = list()  # lista temporária, serve apenas p/ pegar a info e repassar para a a lista GERAL
pesadolist = list()
pesolist = list()
levlist = list()
tot = 0
while True:
    dado.append(input(str('Nome: ')))  # dado é uma info temporária que será armazenada na lista GERAL
    dado.append(int(input('Digite o Peso: ')))
    geral.append(dado[:])  # COPIA a informação da list DADO p/ GERAL
    pesolist.append(dado[:])
    tot += 1  # total idade cadastradas
    for p in pesolist:
        if p[1] > 85:
            pesadolist.append(dado[:])  # adiciona a pessoa e seu peso na lista PESADO
        else:
            levlist.append(dado[:])  # adiciona a pessoa e seu peso na lista LEVLIST
    r = input('Quer continuar? [s/n]:').lower()
    if r == 'n':
        break
    dado.clear()  # limpa a lista DADO, para nao repassar a info duplic p/ a GERAL
    pesolist.clear()
print('+=+' * 20)
print(f'Total de idade cadastradas: {tot}')
print(f'Pessoas acima de 85 kg: {pesadolist}')
print(f'Pessoas abaixo de 85 kg: {levlist}')"""

# 2º MÉTODO: GUANABARA

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [s/n]: '))
    if resp in 'Nn':
        break
print('=-=' * 20)
print(f'Ao todo foram cadastradas {len(princ)} idade')
print(f'O maior peso foi de {mai} kg.', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print('')
print(f'O menor peso foi de {men} kg.', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
