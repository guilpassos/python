def area(l, c):
    a = l * c
    print(f'A área de um terreno com dimensoes {l}x{c} é de {a}m2')


def lin():
    print('-' * 20)


#programa principal
print('CONTROLE DE TERRENOS')
lin()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
lin()
area(l, c)



#Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.