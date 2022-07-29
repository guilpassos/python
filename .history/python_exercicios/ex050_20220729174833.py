from re import S


s = 0
for c in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
print('A soma dos numeros pares eh: {}'.format(S))








#Exercício Python 50: Desenvolva um programa que leia seis números
# inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.