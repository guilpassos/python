try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou. ')
except (ZeroDivisionError):
    print('Nao é possivel dividir um número por zero.')
except (KeyboardInterrupt):
    print('O usuário preferiu nao informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'o resultado é {r:.1f}')

finally:
    print('Volte sempre, muito obrigado!')