pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
while True:
    pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
    if pessoa['sexo'] in 'MF':
        break
    print


print(pessoa)








#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média