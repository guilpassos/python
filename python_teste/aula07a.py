n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {} e a divisao vale {:.3f}'.format(s, m, d), end=' ')
print('Ainda temos a divisao inteira que vale {} e a exponenciacao que é {}'.format(di, e))
