teste = list()
teste.append('Guilherme')
teste.append(30)
galera = list()
galera.append(teste[:])
teste[0] = 'Nathalia'
teste[1] = 31
galera.append(teste[:])
print(galera)
.