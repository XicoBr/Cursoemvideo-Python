# ler nome, sexo e idade de várias pessoas e guardar tudo em  dicionários, e guardar os dicionários em uma lista
# mostrar total de pessoas cadastradas
# mostrar a média de idade do grupo
# mostrar uma lista com todas as mulheres
# mostrar pessoas com idade acima da média

nome = dict()
sexo = dict()
idade = dict()
pessoas = list()
pessoas_fatiamento = list()
total_mulheres = 0
idade_soma = 0
idade_media = 0
continue_check = 's'
contador = 1
while continue_check == 's':
    nome[f'pessoa {contador}'] = input('Nome: ')
    pessoas.append(nome[f'pessoa {contador}'])
    while True:
        sexo[f'pessoa {contador}'] = input('Sexo [m/f]: ').upper()[0]  # [0] puxa apenas o primeiro caractere
        if sexo[f'pessoa {contador}'] in 'MF':
            pessoas.append(sexo[f'pessoa {contador}'])
            break
        print('Erro! Digite novamente!')
    if sexo[f'pessoa {contador}'] == 'F':
        total_mulheres += 1
    idade[f'pessoa {contador}'] = int(input('Idade: '))
    pessoas.append(idade[f'pessoa {contador}'])
    idade_soma += idade[f'pessoa {contador}']
    contador += 1
    continue_check = input('Quer continuar? [s/n]: > ').lower()
    print('-=' * 15)


idade_media = idade_soma / len(nome)
for i in range(0, len(pessoas), 3):  # Fatiamento da lista pessoas em outra lista, já arrumada, agrupada de 3 em 3
    fatiamento = pessoas[i: i + 3]  # Fatiamento indo do índice = i até i + 3, e continua
    pessoas_fatiamento.append(fatiamento)

for sublista in pessoas_fatiamento:  # para sublista de pessoas na lista pessoas_fatiamento
    print(sublista)

print(f'Total de pessoas cadastradas: {contador - 1}')
print(f'Soma das idades: {idade_soma}.')
print(f'Média das idades: {idade_media:.2f} anos.')
print(f'Total de mulheres cadastradas: {total_mulheres}')
