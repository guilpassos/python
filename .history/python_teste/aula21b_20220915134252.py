def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial(2)
print(f'Os resultados dos factoriais sao: {f1}, {f2} e {f3}')


#n = int(input('Digite um número: '))
#print(f'O factorial de {n} é igual a {factorial(n)}')