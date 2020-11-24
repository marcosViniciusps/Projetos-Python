# Este programa le uma frase e confere se ela é um palíndromo desconsiderando os espaços
# Exemplos de palíndromos: "A torre da derrota" , "O lobo ama o bolo"
f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
frase = ''.join(palavras)
inverso = frase[::-1]
'''inverso = ''
print(frase)
for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]
'''
if inverso == frase:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

