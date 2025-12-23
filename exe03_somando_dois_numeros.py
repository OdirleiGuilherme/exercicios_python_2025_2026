from time import sleep
parcela1 = int(input('digite a primeira parcela: '))
parcela2 = int(input('Agora a segunda parcela:  ' ))
print('Agora realizarei a soma das parcelas e vou imprimir o resultado em tela... ')
sleep(2)
soma = parcela1 + parcela2

print('O resultado da soma entre {} e {} é igual à {}'.format(parcela1,parcela2,soma))