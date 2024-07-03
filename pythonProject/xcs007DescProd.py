prod = float(input('Digite o preço do produto: R$ '))
desc = prod - ((5/100) * prod)
print(f'Preço do produto: R${prod}.\nPreço com desconto: R${desc:.2f}')