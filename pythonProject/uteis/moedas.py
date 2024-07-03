def formata(valor, check=False):
    if check:
        formatou = f'{int(valor):.2f}'
        forma_final = f'R$ {str(formatou).replace(".", ",")}'
        return forma_final
    else:
        return valor


def metade(valor, check=False):
    if check:
        formatou = f'{int(valor / 2):.2f}'
        forma_final = f'R$ {str(formatou).replace(".", ",")}'
        return forma_final
    else:
        return valor / 2


def dobro(valor, check=False):
    if check is True:
        formatou = f'{int(valor * 2):.2f}'
        forma_final = f'R$ {str(formatou).replace(".", ",")}'
        return forma_final
    else:
        return valor * 2


def aumenta10(valor):
    return valor * 1.1


def diminui10(valor):
    return valor * 0.9


def resumo(valor, aumento, reducao):

    valor_string = str(valor).replace(".", ",")
    texto_intro = 'RESUMO DO VALOR'
    dobro = valor * 2
    metade = str(valor / 2).replace(".", ",")
    aumento_valor = str(valor + (valor * (aumento / 100))).replace(".", ",")
    reducao_valor = str(valor - (valor * (reducao / 100)))
    linha = ('-' * (len(texto_intro) + 10))
    print(linha)
    print(texto_intro.center(len(linha)))
    print(linha)
    print(f"Preço analisado: {f'R$ {valor_string}':>20}")
    print(f"Dobro do preço: {f'R$ {dobro}':>20}")
    print(f"Metade do preço: R$ {metade:>7}")
    print(f"{aumento}% de aumento: R$ {aumento_valor}")
    print(f"{reducao}% de redução: R$ {reducao_valor}")
    print(linha)
# def formata(funcao):
#     formatou = f'{int(funcao):.2f}'
#     forma = str(formatou)
#     return f"R$ {forma.replace(".", ",")}"
