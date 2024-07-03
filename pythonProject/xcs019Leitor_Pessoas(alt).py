pessoas = dict()
galera = []
continue_check = 'S'
soma_idade = media_idade = 0
while True:
    pessoas['nome'] = str(input('Digite o nome: ')).upper().strip()

    while True:
        pessoas['sexo'] = str(input('Digite o sexo [m/f]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break

        print('-=' * 10)
        print('Erro! Digite M ou F!')
        print('-=' * 10)
    pessoas['idade'] = int(input('Digite a idade: '))
    soma_idade += pessoas['idade']
    galera.append(pessoas.copy())  # adiciona uma cópia do dicionário 'pessoas' à lista 'galera'
    while True:
        continue_check = str(input('Quer continuar? [s/n]: > ')).upper()[0]
        if continue_check in 'SN':
            break
        print('Erro! Digite S ou N!')
    if continue_check in 'Nn':
        break
print(f'Total de pessoas cadastradas: {len(galera)}')
media_idade = soma_idade / len(galera)
print(f'Média de idade: {media_idade:.2f}')
print(f'Mulheres cadastradas: ', end=' ')
for p in galera:  # p = pessoa na lista galera
    if p['sexo'] in 'F':
        print(f'[{p['nome']}]', end='  ')
print()
print('Pessoas acima da média de idade: ', end='')
for p in galera:
    if p['idade'] > media_idade:
        print(f'[Nome: {p['nome']} - Idade: {p['idade']} anos ] |', end=' ')
print()
