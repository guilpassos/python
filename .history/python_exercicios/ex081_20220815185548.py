valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'nN':
        break

print(f'Foram digitados {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente sao {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 nao foi encontrado na lista.')



#Exercício Python 081: Crie um programa que vai ler vários
# números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.