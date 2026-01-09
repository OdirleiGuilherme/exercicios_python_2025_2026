# trabalahando com Tuplas
# Tuplas são imutáveis
# aplicaremos aqui o index()

a = (2,4,6,8,9)
b = (1,3,5,7,9,10)
c = b + a
# Reparem que inverti A + B para B + A, ou seja, será apresentado primeiro os itens de B e depois de A
# E quando juntar todos na ordem que devem ficar o index de 8 que anteriormente era 3 passou para 9
# pelo motivo de itens de A serem apresentados depois de B
print(c)
print(c.index(8))

# Reparem que inverti A + B para B + A, ou seja, será apresentado primeiro os itens de B e depois de A
# E quando juntar todos na ordem que devem ficar o index de 8 que anteriormente era 3 passou para 9
# pelo motivo de itens de A serem apresentados depois de B

print(c.index(9,5))
