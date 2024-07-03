''' n1 = int(input('Digite o N1: '))
n2 = int(input('Digite o N2: '))
n3 = int(input('Digite o N3: '))
lista = [n1, n2, n3]
print(f'O menor número é {min(lista)}')
print(f'O maior número é {max(lista)}') '''

# também pode ser:
n1 = int(input('Digite o N1: '))
n2 = int(input('Digite o N2: '))
n3 = int(input('Digite o N3: '))
# verificando quem é menor
menor = n1 # seto o n1 como menor a título de referencia apenas
if n2 < n1 and n2 < n3: # aqui faz-se uma comparação com as outras 2 variáveis
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
