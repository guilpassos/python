matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l], [c]}: '))
print('-=' * 30)
print('A matriz para os valores digitados é:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
for l in range(0, 3):
    
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares da matriz é igual a: {spar}')
print(f'A soma dos valores da terceira coluna é igual a: {scol}')
print(f'O maior valor da segunda linha é: {mai}')            
 






#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.