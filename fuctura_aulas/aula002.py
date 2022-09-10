emprestimo = float(input('Valor do empréstimo: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
if emprestimo <= (salario * 0.5):
    print('Seu empréstimo foi aprovado!')
elif emprestimo <= (salario * 0.75):
    print('Situacao em análise!')
else:
    print('Nao foi possível aprovar seu empréstimo')
