print('GERADOR DE PA')
print('-=' * 10)
a1 = int(input('Primeiro termo da Progressao: '))
r = int(input('Razao da Progressao: '))
an = a1
contador = 1
while contador <= 10:
    print('{} -> '.format(an), end='')
    an += r
    contador += 1
print('FIM')




#an = a1 + (n - 1) * r


#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.