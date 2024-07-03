tab = ('palmeiras', 'grêmio', 'atlético-mg', 'flamengo', 'botafogo', 'bragantino',
       'fluminense', 'atletico-pr', 'internacional', 'fortaleza', 'são paulo',
       'cuiabá', 'corinthians', 'cruzeiro', 'vasco da gama', 'bahia', 'santos',
       'goiás', 'coritiba', 'america-mg')
print('Tabela Brasileirão 2023:')
for t in (tab):
    print(t.upper())
print('=-=' * 20)
print(f'Top 5: {tab[0:5]}')
print('=-=' * 20)
print(sorted(tab))
print('=-=' * 20)
print(f'Z4: {tab[-4:]}')
print('=-=' * 20)
print(f'São Paulo está na {tab.index('são paulo') + 1}ª posição ')