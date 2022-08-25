num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados: {num[]}')
print(f'Os valores impares digitados: {num[1]}')














#Exercício Python 085: Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.
