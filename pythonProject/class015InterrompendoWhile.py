# Interrompendo repetições while
# while True:
    # if "troféu:
        # pula
        # break (break joga pra fora da estrutura de repetição)

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
