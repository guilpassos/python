s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('Voce informou {} numeros pares e a soma deles eh igual a: {}'.format(cont, s))





#Exercício Python 50: Desenvolva um programa que leia seis números
# inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.