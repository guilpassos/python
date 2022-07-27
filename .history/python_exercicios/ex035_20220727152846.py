print('-=' * 20)
print('Analisador de triangulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento'))
if a < b + c and b < a +c and c < b +a:
    print('Os segmentos acima PODEM CRIAR UM TRIANGULO!!!')
else:
    print('Os segmentos acima NAO PODEM CRIAR UM TRIANGULO!!!')
    