n = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 10):
    r = n * c
    print('{} x  {} = {}'.format(n, c, r))