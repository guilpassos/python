def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

def lin():
    print('-' * 30)


#programa principal
lin()
valores = [6, 5, 2, 1, 4]
print(valores)
lin()
dobra(valores)
print(valores)
lin()