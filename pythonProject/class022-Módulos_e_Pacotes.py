# Modularização : criação de módulos e funções
# lembrar que módulos são diferentes de pacotes
# para exemplo, criei uma pasta chamada UTEIS, e dentro dela criei um arquivo.py chamado NUMEROS, onde há algumas
# funções que foram importadas para esta aula, resultando em uma MODULARIZAÇÃO.
# Um pacote é um conjunto de módulos divididos em setores
from uteis import numeros

num = int(input('Digite um número inteiro: '))
print(f"O fatorial de {num} é {numeros.fatorial(num)}")
print(f"O dobro de {num} é {numeros.dobro(num)}")
print(f"O triplo de {num} é {numeros.triplo(num)}")
