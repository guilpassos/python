from datetime import datetime
from queue import PriorityQueue
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
print(dados)
for k, v in dados.items():
    print(f)







#Exercício Python 092: Crie um programa que leia nome, ano de nascimento
# e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.