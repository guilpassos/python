from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
     [ 1 ] Somar
     [ 2 ] Multiplicar
     [ 3 ] Maior
     [ 4 ] Novos numeros
     [ 5 ] Sair do programa''')
    opcao = int(input('>>>>>>>>Qual a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto de {} x {} é igual a {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            print('O valor {} é o maior.'.format(n1))
        elif n1 < n2:
            print('O valor {} é o maior.'.format(n2))
        elif n1 == n2:
            print('O valores sao iguais!')
    elif opcao == 4:
        print('Informe os novos valores')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opcao inválida! Tente novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')






#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.