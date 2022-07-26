frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posicao {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posicao {}'.format(frase.rfind('A')+1))

#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
