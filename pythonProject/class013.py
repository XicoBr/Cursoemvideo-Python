# Laços de Repetição (for) ou Iteração
'''for c in range(6, -1, -1):#o número no final configura quantos passos serão dados. Se negativo, faz o inverso do positivo
    print(c)
print('FIM')'''

'''inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim + 1, passo):#aqui, adiciona-se 1 ao FIM para termos a contagem indo até exatamente a última letra
    print(c)
print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n # é igual a s = s + n
print('O somatório de todos os números é igual a', s)