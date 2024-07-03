
print(f'{" DETECTOR DE PALÍNDROMO ":=^55}')  # essa config é muito importante, tentar lembrar como fazer sempre
# frase = str(input('Digite a frase: ')).upper().replace(" ", '')
# print(frase)

# método 2

frase = str(input('Digite a frase: ')).upper().strip()
pal = frase.split()
junto = ''.join(pal)  # junta as palavras sem espaço
inverso = ''  # como é string, não se coloca números

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('São palíndromos')
    print(junto, inverso)
else:
    print('Não são palíndromos')
