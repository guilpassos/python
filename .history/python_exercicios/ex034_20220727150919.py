salario = float(input('Qual o seu salario? R$'))
if salario <= 1250:
    novo = salario * 1.15
else:
    novo = salario * 1.1
print('Seu salario passa de R${:.2f} para R${:.2f}'.format(salario, novo))






#Exercício Python 34: Escreva um programa que pergunte o salário
# de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%