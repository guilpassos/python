def soma (*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somamndo os valores {valores} temos {s}.')
#desempacotamento: usando o '*' no parametro da funcao posso utilizar varios valores como referencia para a funcao.

def lin():
    print('-' * 30)

#programa principal
lin()
soma(9, 4)
lin()
soma(2, 1, 7)
lin()
soma(5, 4, 9)
lin()