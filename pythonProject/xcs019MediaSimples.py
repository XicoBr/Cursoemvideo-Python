final = dict()  # ou usa-se {}
final['Nome'] = str(input('Digite o nome: '))
final['Media'] = float(input('Digite a Média: '))
if final['Media'] >= 7:
    final['Situação'] = 'Aprovado(a)'
elif 6 <= final['Media'] <= 6.9:
    final['Situação'] = 'Recuperação'
else:
    final['Situação'] = 'Reprovado(a)'
for k, v in final.items():
    print(f' - {k} é igual a {v}')

