num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'nN':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('=-' * 30)
print(f'A lista completa: {num}')
print(f'A lista com números pares: {par}')
print(f'A lista com números ímpares: {impar}')




#Exercício Python 082: Crie um programa que vai ler vários números
# e colocar em uma lista. Depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.