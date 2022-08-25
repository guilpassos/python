pessoas = {'Nome': 'Guilherme', 'sexo': 'M', 'Idade': '30'}
pessoas['peso'] = 84
# Nao precisar de append pra adicionar elemento nos dicionarios

for k, v in pessoas.items():
    print(f'{k} = {v}')

#for v in pessoas.values():
#   print(v)


#for k in pessoas.keys():
#    print(k)

#print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())