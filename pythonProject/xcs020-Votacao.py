# usar funçao, que recebe o ano de nascimento do usuario
# saída será se o voto é obrigatório, opcional ou não tem idade para votar


def votacao():
    from datetime import date

    ano_atual = date.today().year
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if 18 <= idade < 65:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO!'
    elif (16 <= idade < 18) or (idade > 65):
        return f'Com {idade} anos, o voto é OPCIONAL!'
    elif idade < 16:
        return f'Com {idade} anos, ainda não poderá votar!'


print(votacao())
