valor = 0
total = int(input('valor do saque: '))
if total % 50 != 0:
    valor = (total / 50)
    print(f'{valor:.0f}')
