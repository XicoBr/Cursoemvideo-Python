# Fatorial

def fatorial(numero, show=False):
    """
    -> Calcula a fatorial de um número
    :param numero: o numero a ser calculado
    :param show: mostrar ou não a conta
    :return: o valor fatorial de numero
    """
    fat = 1
    if show is False:
        for contador in range(numero, 0, -1):
            fat *= contador
        return fat
    elif show is True:
        for index in range(numero, 0, -1):
            print(f'{index}', end=' ')
            if index != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        for contador in range(numero, 0, -1):
            fat *= contador
        return fat


f1 = fatorial(5, True)
print(f1)
f2 = fatorial(4)
print(f2)
f3 = fatorial(6, True)
print(f3)
help(fatorial)
