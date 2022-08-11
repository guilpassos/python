núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Voce digitou os valores: {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O número 3 aparece na posicão {núm.index(3) + 1}')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print(f'Os números pares foram: ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')

#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.