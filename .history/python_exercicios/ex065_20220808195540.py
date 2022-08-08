resposta = 'S'
media = soma = cont = maior = menor = 0
while resposta in 'sS':
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    maior = n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('FIM')
print('Voce digitou {} numeros e a media entre eles eh igual a {}. O maior valor eh {} e o menor eh {}'.format(cont, media, maior, menor))



#Exercício Python 65: Crie um programa que leia vários números
# inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.