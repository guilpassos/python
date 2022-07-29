print('=' * 40)
print('10 TERMOS DE UMA PROGRESSAO ARITMETICA')
print('=' * 40)
a1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razao da PA: '))
n = 1
print('O termo a1 da Progressao Aritmetica eh igual a: {}'.format(a1))
for c in range(1, 10):
    n += 1
    an = a1 + (n - 1) * r
    print('O termo a{} da Progressao Aritmetica eh igual a: {}'.format(n, an))




#Exercício Python 51: Desenvolva um programa que leia o primeiro
# termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.
# an = a1 + (n – 1) r