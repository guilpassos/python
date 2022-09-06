def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} números.')


def lin():
    print('-' * 30)


#programa principal
lin()
contador(5, 5, 1)
lin()
contador(1, 8)
lin()
contador(3, 6)