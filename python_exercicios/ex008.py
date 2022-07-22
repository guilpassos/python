n = float(input('Uma medida em metros: '))
print('A medida de {:.0f} metros equivale a\n{:.3f}km\n{:.2f}hm\n{:.1f}dam'.format(n, n*0.001, n*0.01, n*0.1))
print('{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(n*10, n*100, n*1000))

