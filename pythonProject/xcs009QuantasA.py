a = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {a.count('A')} vez(es)')
print(f'A1 aparece na posição {a.find('A')+1}')
print(f'A ultima A aparece na posição {a.rfind('A')}')
#print(f'A ultima letra A aparece na posição {a[-1]}')
#aparentemente, pra letras não há a possibilidade de usar o [-1] para localizar a letra desejada na ultima posição
