print('-=' * 20)
print('Analisador de Triangulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM formar um triangulo ', end='')
    if a == b and b == c:
        print('EQUILATERO!')
    if a != b and a != c and b!= c:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima NAO PODEM criar um triangulo!')


#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes