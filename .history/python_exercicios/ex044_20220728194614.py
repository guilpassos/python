print('{:=^40}'.format('LOJAS PASSOS'))
preco = float(input('Valor da compra: R$'))
print('O produto custa R${:.2f}' .format(preco))
print('''FORMAS DE PAGAMENTO
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA NO CARTAO
[ 3 ] 2X NO CARTAO
[ 4 ] 3X  OU MAIS NO CARTAO''')
opcao = int(input('Qual a opcao de pagamento? '))
if opcao == 1:
    total = preco * 0.9
    print('O valor da compra de R${:.2f} com desconto sera: R${:.2f}!'.format(preco, total))
elif opcao == 2:
    total = preco * 0.95
    print('O valor da compra de R${:.2f} com desconto sera: R${:.2f}'.format(preco, total))
elif opcao == 3:
    print('O valor da compra sera dividido em 2x e sera: R${:.2f}'.format(preco))
elif opcao == 4:
    total = preco * 1.2
    parcela = int(input('Quantas parcelas? '))
    print('O valor da compra de R${:.2f} vai ser dividido em {}x COM JUROS'.format(preco, parcela))
    print('O valor da compra passa a ser: R${:.2f}'.format(total))



#Exercício Python 44: Elabore um programa que calcule o valor
# a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros