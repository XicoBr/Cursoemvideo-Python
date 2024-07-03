cores_fonte = {'white': '\033[0;30;47m',
               'black-blue': '\033[0;30;44m',
               'green': '\033[1;30;42m',
               'reset': '\033[0m',
               'black-green': '\033[0;30;42m',
               'black-red': '\033[0;30;41m',
               'padrao': '\033[m',
               'yellow': '\033[1;30;43m'}




def ajuda(com):

    titulo(f'Acessando o manual do comando \'{com}\'')
    print(cores_fonte['white'], end='')
    help(com)
    print(cores_fonte['reset'], end='')

def titulo(msg, cor='padrao'):
    tam = len(msg)
    print(cores_fonte[cor], end='')
    traco = ('~' * (tam + 4))
    print(traco)
    print(msg.center(len(traco)))
    print(traco)
    print(cores_fonte['reset'], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca >> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

print(cores_fonte['black-red'], end='')
titulo('Até logo!')
print(cores_fonte['reset'], end='')

# print(manual_len)
