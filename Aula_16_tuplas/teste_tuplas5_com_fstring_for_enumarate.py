# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza','Pudim','Batata Frita', 'Açai')

for pos,comida in enumerate(lanche):
    print(f'Organizei os lanches com númerações {comida} é número {pos}')