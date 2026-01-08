# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza','Pudim','Batata Frita', 'Açai')

# print(lanche [3])

# atribuindo um FOR
#for comida in lanche:
#    print(f'Vou comprar na lanchonete {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])
print('Gastei uma grana!')