# Tuplas são variáveis compostas e IMUTÁVEIS e utilizam PARENTESES
lanche = ('hamburguer', 'suco', 'pizza', 'pudim') # lanche = tuple()
print(lanche)  # mostra todos os valores
print(lanche[0])  # mostra apenas o primeiro valor
print(lanche[0:2])  # mostra apenas os 2 primeiros valores
print(lanche[-1])  # mostra apenas o último valor
print(lanche[1:])  # mostra o segundo valor até o último
print(lanche[:4])  # mostra do inicio até o ultimo elemento
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
print(len(lanche))  # mostra o comprimento da variável
#for c in range(0, len(lanche)):  # c = comida; c nao foi declarado, python cria automatico
    #print(lanche[c])
# Lembrar que na hora de referenciar, utilizar colchetes. Ex:
# print(lanche[0])
# TUPLAS são IMUTÁVEIS
print(sorted(lanche))  # mostra os elementos em ordem alfabética
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)  # vai fazer a união dos conjuntos
print(c.index(8))  # mostra a posição da variável
pessoa = ('Diego', 26, 'M', 88)  # Python aceita diversos tipos de valores em uma só variável
print(pessoa)
del (pessoa)  # deleta a variável, pode-se apagar uma tupla inteira, não apenas uma parte dela