# deve ler o nome,ano nascimento, e carteira de trabalho
# se ctps = 0, quebra o programa
# se ctps != 0, ler ano de contratação e salário
# retorna a idade minima para se aposentar (ex = 35 anos de contribuição)

from datetime import datetime

data_atual = datetime.now()
ano_atual = data_atual.year
pessoas = dict()  # ou {}


pessoas['nome'] = str(input('Nome: '))
pessoas['ano_nascimento'] = int(input('Ano de nascimento: '))
pessoas['ctps'] = int(input('Código da Carteira de Trabalho [00 se não possui]: '))

if pessoas['ctps'] == 00:
    print('Você não possui o beneficio do FGTS')

else:
    pessoas['ano_contratação'] = int(input('Ano de contratação: '))
    pessoas['salario'] = float(input('Salário: R$ '))
    pessoas['idade_aposentadoria'] = pessoas['ano_contratação'] - pessoas['ano_nascimento'] + 35
    print('-=' * 20)
    for k, v in pessoas.items():
        print(f'{k}: {v}')
