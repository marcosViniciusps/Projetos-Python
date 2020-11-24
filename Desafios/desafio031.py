# Este programa pergunta a distância da viagem e calcula o seu preço conforme abaixo:
# Será cobrado 0.50R$ por Km caso a viagem seja de até 200Km
# Será cobrado 0.45R$ por Km caso a viagem seja maior que 200Km
d = float(input('Digite a distância da viagem: '))

if d > 200:
    print(' Esta é uma viagem longa, será cobrado: {:.2f}R$ pelos {}Km'.format((d*0.5),d))
else:
    print(' Esta é uma viagem curta, será cobrado: {:.2f}R$ pelos {}Km'.format((d*0.45),d))
