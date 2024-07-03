# utilizar desempacotamento para identificar o maior numero entre os fornecidos
# utilizar asterico no parametro da função para usar vários valores de uma vez
# mostrar o total de números passados e o maior entre eles
from time import sleep


def maior_numero(* numero):
    # print(f'O maior número é {max(numero)}')  # uma das formas de se fazer

    total_num = maior_numero = 0
    print(f'Analisando os valores: {numero}')
    for i in range(0, 3):
        print('.', end='')
        sleep(1)
    print()
    for valor in numero:
        if valor > maior_numero:
            maior_numero = valor
        total_num += 1
    print(f'Total de números analisados: {total_num}')
    sleep(1)
    print(f'Maior número: {maior_numero}')
    sleep(1)
    print('-=' * 15)
    print('Contagem finalizada!')


maior_numero(5, 4, 3, 2, 1, 2)
maior_numero()