num = int(input('Digite um número para realizar a fatoração: '))
c = num  # esse é o contador
f = 1  # valor para multiplicação(sempre que for multiplicar, usar 1
print(f'{num}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')  # lembrar desse print que é bom pacarai
    f *= c
    c -= 1  # recebe -1 para ir até o número 1, aí o contador finaliza
print(f, end='')
