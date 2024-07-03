# ADICIONAR NUMERO EM LISTA, E JÁ FAZER COM QUE SEJA ORGANIZADO DE FORMA CRESCENTE, SEM USO DO SORT. COMO FAZER?
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:  # se n maior que último valor
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):  # enquanto pos for menor que o tot de elem. da lista
            if n <= lista[pos]:  # se numero for menor que o numero na pos.
                lista.insert(pos, n)  # adiciona o número na posição
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')
