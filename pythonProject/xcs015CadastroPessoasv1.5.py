# CADASTRO DE PESSOAS v1.5
men = women = idade = women20 = age18 = 0
r = ''
while True:
    sexo = input('Digite o sexo [m/f]: ').lower()
    while sexo != 'm' and sexo != 'f':
        sexo = input('Opção inválida! Digite novamente: ')
    idade = int(input('Digite a idade: '))
    print('=-=' * 20)
    if sexo == 'm':
        men += 1
    elif sexo == 'f':
        women += 1
        if idade < 20:
            women20 += 1
    if idade >= 18:
        age18 += 1
    r = input('Quer continuar? [s/n]: ').lower()
    print('=-=' * 20)
    while r != 's' and r != 'n':
        r = input('Opção inválida! Quer continuar? [s/n]: ').lower()
    if r == 'n':
        break
print(f'Homens: {men}')
print(f'Mulheres abaixo de 20 anos: {women20}')
print(f'Pessoas maiores de 18 anos: {age18}')
