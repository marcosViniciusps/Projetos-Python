# Este programa conta quantas vezes a letra 'a' aparece em uma string sua primeira e última posição
frase = str(input('Digite uma frase: ')).strip().lower()
print('A frase digitada possui {} letra(s) a'.format(frase.count('a')))
print('A primeira letra a esta na posição: {}' .format(frase.find('a')))
print('A ultima letra a apareceu na posição: {}'.format(frase.rfind('a')))
