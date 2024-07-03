from datetime import date
print('=-=' * 20)
print(f'{'ALISTAMENTO MILITAR':>40}')
print('=-=' * 20)
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
if idade < 18:
    saldo = 18 - idade
    print(f'Você tem {idade} anos e o alistamento não é obrigatório.')
    if saldo <= 1:
        print(f'Falta {saldo} ano para o seu alistamento')

    else:
        ano = atual + saldo
        print(f'O seu alistamento será em {ano}')

elif idade == 18:
    print(f'Você completará 18 anos em {atual} e o alistamento é obrigatório.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você tem {idade} anos e o seu alistamento foi há {saldo} anos, em {ano}.')
