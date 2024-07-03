nome = (input('Digite seu nome: ')).strip().upper()
div = nome.split()
sil = 'SILVA' in div
print('Seu nome tem SILVA?', '[', 'SILVA' in div, ']')
print(f'Há {len(nome) - nome.count(' ')} letras')
