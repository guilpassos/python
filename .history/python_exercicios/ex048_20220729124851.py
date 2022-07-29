s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        s = c
print('A soma de todos os {} valores soicitados: {}'.format(contador, s))



#Exercício Python 48: Faça um programa que calcule a soma
# entre todos os números IMPARES que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.