salario_atual = float(input('Digite seu salário atual antes de ter acesso ao seu salário atualizado: '))
aumento = (salario_atual * 0.15)
salario_atualizado = (salario_atual + aumento)

print('Você teve uma atualização de 15% de aumento ficando com o salário de {:.2f} reais'.format(salario_atualizado))