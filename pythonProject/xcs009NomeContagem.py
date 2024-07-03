nome = str(input('Digite seu nome: ')).strip()
print(f'O seu nome em maiusculo é: {nome.upper()}')
print('O nome com as letras em minúsculo: ', nome.lower())
print('Total de letras: ', (len(nome) - nome.count(" ")))
div = nome.split()
print('Primeiro nome: ', (div[0]))
print('Letras no primeiro nome: ', (len(div[0])))
#primeiro nome pode ser
#print(Seu primeiro nome é, nome.find(" ")), uma vez que ele contará a primeira palavra a partir do primeiro espaço
