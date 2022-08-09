cont_i = 0
cont_h = cont_m = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip()[0].upper()
    tipo = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
    print('='*30)
    if idade > 18:
        cont_i += 1
    if sexo in 'mM':
        cont_h += 1
    if sexo in 'fF' and idade < 20:
        cont_m += 1
    if tipo in 'nN':
        break
print(f'{cont_i} pessoas tem mais de 18 anos.')
print(f'{cont_h} homens foram cadastrados.')
print(f'{cont_m} mulheres tem menos de 20 anos.')

#Exercício Python 69: Crie um programa que leia a idade e o sexo
# de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.