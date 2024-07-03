import math # from math import floor, sqrt (importa apenas as funções de arredondar pra baixo e raiz quadrada

import emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é {raiz:.2f}')
# caso seja feita a importação otimizada, não é necessário o uso de math., apenas o comando.
print(emoji.emojize('Bora almoçarrr! :fork_and_knife:'))