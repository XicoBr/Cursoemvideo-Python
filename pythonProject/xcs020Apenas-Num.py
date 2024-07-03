cores = {'red_strt': '\033[31;1m', 'red_end': '\033[m'}


def leiaint(valor):
    while True:
        valor_fim = input(valor)
        if valor_fim.strip().isnumeric():
            return f'{valor_fim}'  # o return funciona como um break, entao no caso return = break

        else:
            print(f'{cores['red_strt']}ERRO! Digite um número inteiro válido.{cores['red_end']}')


n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')
