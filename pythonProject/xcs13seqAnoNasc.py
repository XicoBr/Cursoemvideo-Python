from datetime import date
atual = date.today().year
contmen = 0
contmai = 0
for cont in range(1, 8):
    ano = int(input(f'P{cont} - Digite o ano de nascimento: '))
    idade = atual - ano
    if idade >= 18:
        contmai += 1
    if idade < 18:
        contmen += 1
print(f'Número de pessoas maiores de 18 anos: {contmai}')
print(f'Número de pessoas menores de 18 anos: {contmen}')
