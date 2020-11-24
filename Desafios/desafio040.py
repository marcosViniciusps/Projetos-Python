# Este programa le duas notas de um aluno e retorna sua média e se ele foi aproovado
# Uma media menor que 5 gera reprovação e uma nota maior que 7 aprova o aluno
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('Sua média foi de: {:.2f}'.format(media))
if media < 5:
    print('Reprovado!')
elif media > 7:
    print('Aprovado!')
else:
    print('Voçê está de recuperação! ')
