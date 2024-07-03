# LISTAS
# Índice = posição na lista
# valor = elemento da lista
comida = ['pizza', 'suco', 'bolo']  # LEMBRAR QUE LISTAS USAM COLCHETES! var = list()
print(f'Lista INICIAL: {comida}')
comida.insert(0, 'cookie')
print(f'Valor [cookie] inserido na posição 0: {comida}')
comida.append('agua')
print(f'Adiciona valor [água] na última posição: {comida}')
comida.sort()
print(f'Organiza a lista em ordem alfabética: {comida}')
comida.pop()
print(f'Exclui o último elemento : {comida}')
print('=-=' * 20)
num = [3, 6, 9, 2, 4]
print(f'LISTA INICIAL DE NÚMEROS: {num}')
num.sort()
print(f'Números em ordem crescente: {num}')
num[2] = 10
print(f'Troca de valores na posição 2: {num}')
num.append(5)
print(f'Adição do valor [5] na ultima posição: {num}')
num.sort(reverse=True)
print(f'Mostra a lista em ordem reversa: {num}')
print('=-=' * 20)
valor = list(range(3, 11))
print(f'Transforma uma tupla em lista: {valor}')
print('=-=' * 20)
'''valores = []  # lista vazia
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))  # add valores à lista
for c, v in enumerate(valores):  # c = índice; v = valores
    print(f'Na posição {c} o valor é {v}')
print('=-=' * 20)'''
a = [2, 4, 7, 8, 9]
b = a
# b[2] = 5  # a lista do python faz uma ligação com listas de mesmo valor, p/ contornar isso:
b = a[:]  # aqui, B somente COPIA os valores da lista A
b[2] = 5  # agora a mudança será apenas na lista B
print(f'Lista A: {a}')
print(f'Lista B: {b}')
