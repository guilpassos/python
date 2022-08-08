print('GERADOR DE PA')
print('-=' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razao: '))
an = a1
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(an), end='')
        an += r
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais: '))
print('Progressao finalizada com {} termos mostrados!'.format(total))



#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário
# se ele quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.