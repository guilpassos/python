cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print('O número digitado foi', cont[num])
        pergunta = str(input('Deseja continuar? [S/N] ')).strip()[0].upper()
        if pergunta in 'N':
            break
print('Volte sempre!')
        
  


#Exercício Python 72: Crie um programa que tenha uma dupla totalmente 
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.