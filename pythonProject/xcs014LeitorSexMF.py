sexo = input('Informe o sexo [m/f]: ').strip().lower()[0]
while sexo == 'f' or sexo == 'm':
    sexo = input('Informe o sexo [m/f]: ').lower()
    if sexo != 'f' and sexo != 'm' and sexo != '0':
        sexo = input('Dados Inválidos. Informe o sexo [m/f]: ')
if sexo == '0':
    print('Programa encerrado')
