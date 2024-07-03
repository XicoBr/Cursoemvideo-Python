from time import sleep
f20 = 0
somaid = 0
Midade = 0
media = 0
for p in range(1,6):
    print(f'======= {p}ª PESSOA =======')
    nome = input('Digite o nome :').strip()
    listnome = [nome]
    idade = int(input('Digite a idade: '))
    somaid = somaid + idade
    listida = [idade]
    sexo = str(input('Digite o sexo [m/f]: ')).lower()
    listsex = [sexo]
    if sexo == 'm':
        if idade > Midade:
            Midade = idade
            Mnome = nome
    if sexo == 'f':
        if idade < 20:
            f20 += 1
media = somaid / p
print('=-=' * 20)
print('PROCESSANDO.... POR FAVOR, AGUARDE....')
print('=-=' * 20)
sleep(2)
print(f'A média de idade é de : {media} anos.')
print(f'O nome do homem mais velho é {Mnome} e sua idade é {Midade}')
if f20 >= 1:
    print(f'Há {f20} mulher(es) abaixo de 20 anos.')
if f20 == 0:
    print('Não há mulheres com idade abaixo de 20 anos.')


