velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite de 80km/h!')
    multa = (velocidade-80)*7
    print('Sua multa foi de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com seguranca!')

