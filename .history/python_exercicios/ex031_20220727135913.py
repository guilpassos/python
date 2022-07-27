d = float(input('Qual a distancia da sua viagem? '))
print('Voce está prestes a realizar uma viagem de {:.0f}Km!'.format(d))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('A sua passagem irá custar R${:.2f}'.format(p))
print('Boa viagem!')


#Exercício Python 31: Desenvolva um programa que pergunte
# a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.