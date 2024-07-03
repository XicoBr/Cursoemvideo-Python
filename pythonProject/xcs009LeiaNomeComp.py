nome = str(input('Digite seu nome: ')).upper().strip().split()
print(nome)
print(f'O primeiro nome é: {nome[0]}')

print(f"O ultimo nome é: {nome[-1]}")
# o -1 pode ser usado para representar a ultima letra(ou nome, nesse caso) de uma string, assim como -2 é a penultima, e assim por diante