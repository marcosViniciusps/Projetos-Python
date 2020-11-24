# Este programa possui uma tupla com varios nomes e retorna as vogais que eles contém
palavras = ('aprender','programar','liguagem','python','curso','gratis',
            'estudar','praticar','trabalhar','mercado','programador','futuro')
vogais = ('a','e','i','o','u')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end='')

