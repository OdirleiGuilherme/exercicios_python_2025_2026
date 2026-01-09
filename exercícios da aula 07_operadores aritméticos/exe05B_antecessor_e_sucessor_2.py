from time import sleep

# No exercício exe005.py, acabei usando somente uma variável, mas repliquei o exercício utilizando
# 3 variáveis pelo seguinte fato. E se por erro acabei esquecendo que iria precisar dessas duas
# variáveis mais a frente a antecessor e sucessor, então, que alterar o programa.
# Quando programar, verifique ao criar variáveis se vai precisar no futuro para não ter dor de cabeça.

number = int(input('Digite um número de sua escolha: '))
print('Vamos descobrir seu Predecessor e o seu Sucessor...')
antecessor = number - 1
sucessor = number +1

sleep(2)

print('O número digitado foi {}, que tem como Predecessor o número {} e'
      ' como Sucessor o número {}!'.format(number,antecessor,sucessor))