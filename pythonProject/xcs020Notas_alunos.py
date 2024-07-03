def notas_alunos(* notas, situacao=False):
    """
    notas_alunos(* notas, situação)
    -> Função para analisar várias notas e a situação de vários alunos
    :param notas: 1 ou +1 notas analisadas (float) dos alunos
    :param situacao: mostrar ou não a situação da turma, sendo boa, medíocre e ruim (3 situações)
    :return: um dicionário com: quantidade de notas, maior nota, menor, média, situação(opcional)
    """
    dicionario = dict()
    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    dicionario['media'] = sum(notas) / len(notas)
    if situacao:
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'BOA'
        elif dicionario['media'] >= 5:
            dicionario['situacao'] = 'MEDIOCRE'
        else:
            dicionario['situacao'] = 'RUIM'
    return dicionario


# help(notas_alunos)  # mostra a docstring do programa
f1 = notas_alunos(5, 1, 8, 2, 5, situacao=True)
print(f1)
