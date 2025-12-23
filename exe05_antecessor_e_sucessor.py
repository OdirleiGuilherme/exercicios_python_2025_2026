from time import sleep
number = int(input('Digite um número de sua escolha: '))
print('Vamos descobrir seu Predecessor e o seu Sucessor...')

sleep(3)

print('O número digitado foi {}, que tem como Predecessor o número {} e'
      ' como Sucessor o número {}!'.format(number,(number-1),(number+1)))