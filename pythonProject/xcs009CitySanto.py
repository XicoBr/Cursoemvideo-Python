city = input('Digite o nome da sua cidade: ').strip()#.split() #remove os espaços inuteis e divide as palavras em blocos
#print(city) aqui, as palavras estão separadas
print('Sua cidade começa com a palavra [Santo]?', end='')
print(' [', city[:5].upper() == 'SANTO', ']')
#Lembrar que a contagem sempre começa com 0, então na palavra SANTO temos:
#S A N T O
#0 1 2 3 4 ou seja, na funcão city[:5], começa do inicio(já que não foi especificado) e faz a contagem até o 4º caractere, excluindo o 5º