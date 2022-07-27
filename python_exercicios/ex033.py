a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é o menor
me = a
if b<a and b<c:
    me = b
if c<a and c<b:
    me = c
#Verificando quem é o maior
ma = a
if b>a and b>c:
    ma = b
if c>a and c>b:
    ma = c
print('O menor valor é {}'.format(me))
print('O maior valor é {}'.format(ma))



#Exercício Python 33: Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.