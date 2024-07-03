"""idade = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}  # dict{}
print(f'O {idade["nome"]} tem {idade["idade"]} anos.')
print(idade.keys())  # mostra os ÍNDICES
print(idade.values())  # mostra os VALORES
print(idade.items())  # mostra ÍNDICES e VALORES
for k, v in idade.items():  # função de ENUMERATE das LISTAS e TUPLAS
    print(f'{k} = {v}')"""

"""brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])"""

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).upper()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper()
    brasil.append(estado.copy())  # usa-se .copy() para fazer o FATIAMENTO de um dicionário
for uf in brasil:
    """for k, v in uf.items():  # NECESSÁRIO O USO DE ITEMS() PARA MOSTRAR TODAS AS INFOS
        print(f'O campo {k} tem valor {v}')"""
    for v in uf.values():  # aqui, mostra APENAS os VALORES do dicionário
        print(v, end=' ')
    print()
