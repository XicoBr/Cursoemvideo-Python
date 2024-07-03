# calcular a área de um terreno


def calcula_area():
    comprimento = float(input('Digite o comprimento do terreno em metros: '))
    largura = float(input('Digite a largura em metros: '))
    area = comprimento * largura
    print(f'A área de um terrno de {comprimento} x {largura} é de {area} m².')


calcula_area()
