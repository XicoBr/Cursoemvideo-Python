mult3 = 0
for c in range(1, 500):
    if (c % 2 == 1) and (c % 3 == 0):
        mult3 = mult3 + 1
print(f'Os números multiplos de 3 no intervalo de 1 a 500 é {mult3}')