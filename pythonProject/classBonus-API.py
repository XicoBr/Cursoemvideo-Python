import json
import requests

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()  # transformando o arquivo json em dicionário do python
cotacao_dolar = cotacoes["USDBRL"]["bid"]
#print(cotacoes)
print(cotacao_dolar)
