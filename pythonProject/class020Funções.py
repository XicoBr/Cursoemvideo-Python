def linhas(texto):
    print('-=' * 20)
    print(f'{texto:^40}')
    print('-=' * 20)


linhas('Alunos')

# Usa-se def function(* parameter) para desempacotar vários valores de uma vez. Exemplo:


def soma(* num):
    print(num)


soma(1, 2, 3, 4, 5)
soma(5, 10, 6, 5)


def dobra(lista):
    cont = 0

    while cont < len(lista):
        lista[cont] *= 2
        cont += 1
    print(lista)


teste = [4, 5, 2, 6, 1]
dobra(teste)


def soma_par(* numero):  # Docstrings - utiliza-se aspas 3 vezes para criar a documentação de uma função, que retorna a
    # informação quando usamos >>> print(function.__doc__)
    """
    soma todos os valores que tem resto de divisão = 0 quando divididos por 2
    """

print(soma_par.__doc__)


# DEFININDO VARIÁVEL OPCIONAL

def fatorial(numero=1):  # aqui, ao definirmos n=1, estamos informando ao programa que, se não passarmos nenhum valor,
# o n automaticamente vale 1

    fatorial = 1
    for cont in range(numero, 0, -1):
        fatorial *= cont
    return fatorial


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'O fatorial é igual a {f3}')


print()

def teste(b):
    global a  # ao utilizarmo GLOBAL, estamos informando que aquela variável global, fora da função, vale determinado
    # valor, no caso a = 7 tanto local quanto global
    a = 7
    b += 4
    c =2
    print(f'[A] local vale {a}')
    print(f'[B] local vale {b}')
    print(f'[C] local vale {c}')


a = 5
teste(a)
print(f'[A] global vale {a}')  # aqui, como declaramos dentro da função que a variável "a" é global e definimos um
# valor para ela, automaticamente recebe o valor que está dentro da função
