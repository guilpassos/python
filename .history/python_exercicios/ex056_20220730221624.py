somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    print('------- {}ª PESSOA -------'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('[M/F]: ')).strip()
    somaidade += idade
    if c ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A media das idade do grupo eh de {} anos.'.format(mediaidade))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo {} mulheres no grupo tem menos de 20 anos.'.format(totmulher20))




#Exercício Python 56: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome
# do homem mais velho e quantas mulheres têm menos de 20 anos.