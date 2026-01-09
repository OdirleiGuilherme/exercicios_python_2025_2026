# trabalahando com Tuplas
# Tuplas são imutáveis
# aplicaremos aqui o index()

a = (2,4,6,8,9)
b = (1,3,5,7,9,10)
c = b + a
# Tanto em A como em B temos o número 9 duas vezes como fazemos para descobrir o índice de ambos ao mesmo tempo.
# E quando juntar todos na ordem que devem ficar o index de 8 que anteriormente era 3 passou para 9
# pelo motivo de itens de A serem apresentados depois de B
#print(c)
#print(c.index(9)) # assim achamos o índice do primeiro número 9.

# Bem ao rodar achamos o índice do primeiro 9 e ele tá no índice 4, mas para descobrir o índice do segundo número 9
# fazemos assim, colocamos o primeiro nove que vai identificar o índice 4 clicamos em vírgula e inserimos o 5
# pois ele vai iniciar a contagem do índice 5 até o final para descobrir qual o número de índice tá o proxímo 9
# resultado os números 9 estão nos índices 4 e 10.
print(' Os respectivos números 9 estão nos índices: {} e {}'.format((c.index(9)), (c.index(9, 5))))

