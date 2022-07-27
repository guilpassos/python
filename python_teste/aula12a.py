nome = str(input('Qual o seu nome? '))
if nome == 'Guilherme':
    print('Que nome bonito, {}!'.format(nome))
elif nome == 'Pedro' or nome == 'Joao' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Juliana Marcia Paula':
    print('Belo nome feminino!')
print('Tenha um bom dia, {}'.format(nome))

