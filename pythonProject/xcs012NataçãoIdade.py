'''print('=-=' * 20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('=-=' * 20)
idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print(f'Idade: {idade} anos')
    print('Categoria: Mirim')
elif idade > 9 <= 14:
    print(f'Idade: {idade} anos')
    print('Categoria: Infantil')
elif idade > 14 <= 17:
    print(f'Idade: {idade} anos')
    print('Categoria: Junior')
elif idade > 18 <= 20:
    print(f'Idade: {idade} anos')
    print('Categoria: Sênior')
else:
    print(f'Idade: {idade} anos')
    print('Categoria: Master')'''

from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
mirim = range(4, 9)
infantil = range(10, 14)
junior = range(15, 17)
senior = range(18, 20)
master = range(21, 23)
spa = range(24, 99)
print(f'Idade: {idade} anos')
if idade in mirim:
    print('Categoria: Mirim')
if idade in infantil:
    print('Categoria: Infantil')
if idade in junior:
    print('Categoria: Júnior')
if idade in senior:
    print('Categoria: Sênior')
if idade in master:
    print('Categoria: Master')
if idade in spa:
    print('Não pode participar')
