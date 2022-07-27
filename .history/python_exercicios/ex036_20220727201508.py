casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salario do comprador: R$'))
anos = int(input('Em quantos anos dseja financiar? '))
prestacao = casa / (anos*12)
print('Para pagar uma casa no valor de R${:.2f} em {} anos, a prestacao seria de R${:.2f}'.format(casa, anos, prestacao))
if salario > prestacao * (30 / 100):
    print('EMPRÉSTIMO pode ser CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!')
    
# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.