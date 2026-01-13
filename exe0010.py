real = float(input('\nDigite valor para conversão em dolár: R$ '))
dolar = (real/6.0509001)
dolar2 = (6.0509001 * real)

print('\nCom {:.2f} de Reais seu poder de compra fica em {:.2f} Doláres'.format(real,dolar))

print('\nMas com {:.2f} Doláres temos um poder de compra no Brasil de {:.2f} Reais'.format(dolar,dolar2))