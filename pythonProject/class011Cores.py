#\033[0;33;44m #estilo texto fundo
# ESTILO:
# 0 = nenhum/none
# 1 = negrito/bold
# 4 = sublinhado/underline
# 7 = negativo (inverte as funções)/negative

# COR TEXTO                COR FUNDO
# 30 =        black =========> 40
# 31 =        red   =========> 41
# 32 =        green =========> 42
# 33 =        yellow ========> 43
# 34 =        blue  =========> 44
# 35 =        magenta =======> 45
# 36 =        cyan ==========> 46
# 37 =        grey ==========> 47
# 97 =        white =========> 107
# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[0;30;42m
# \033[m
# \033[7;30m

print('Olá, Mundo!')
print('\033[31mOlá, Mundo!') # lembrar que o padrão sempre será \033[;;m
print('\033[1;33mOlá, Mundo!')
print('\033[1;4;33;40mOlá, Mundo!\033[m') # o comando no final da string coloca o fundo apenas nas palavras
print('\033[7;40mOlá, Mundo!\033[m')
print('\033[7;97mOlá, Mundo!\033[m')
print('\033[97mOlá, Mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[33m{a}\033[m e \033[31m{b}\033[m de 10.')

# lembrar que dá pra transformar as cores em variáveis, para o código ficar clean