n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('A soma vale {} !'.format(s)) OBS: muito melhor usar a fstring
print(f'A soma vale {s}')
