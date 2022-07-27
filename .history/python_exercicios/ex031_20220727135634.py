d = float(input('Qual a distancia da sua viagem? '))
print('Voce está prestes a realizar uma viagem de {:.0f}Km!'.format(d))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('A sua passagem irá custar R${:.2f}'.format(p))
Print('Boa viagem!')