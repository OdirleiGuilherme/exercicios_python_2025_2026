largura = float(input('Digite a altura da parede: ' ))
comprimento = float(input('Digite quantos metros comprimento tem a parede: ' ))
janela = float(input('Digite a área da janela se houver na parede, não havendo digite 0: '))
porta = float(input('Digite a área da porta se houver na parede, não havendo digite 0: '))

metros_quadrados = (largura * comprimento)

tinta = (metros_quadrados - janela - porta) /2

print('Sua parede possui {:.2f} Mt² e será gasto {:.2f} lt de tinta para cobrir a área total'.format(metros_quadrados,tinta))