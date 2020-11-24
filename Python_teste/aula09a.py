# Este programa utiliza algumas funções de manipulação de texto
frase = ' Curso em Vídeo Python '
# O primeiro numero é onde começa
# O segundo é onde tremina
# O terceiro é o passo da string
print(frase[1:15:2])

print(frase.count('o'))
print(frase.upper().count('o'))
print(len(frase))
print(len(frase.strip()))

###          Observaçãp: o replace altera a string da (frase) apenas momentaneamente        ###
print(frase.replace('Python', 'Android'))
print(frase)
# Para alterar de forma definitiva:
frase = frase.replace('Python', 'Android')
print(frase)

####        Para procurar uma palavra na string:           ###
print('Curso' in frase) # Retorna True ou False
# Para procurar uma palavra na string:
print(frase.find('Curso')) # Retorna a posição de início da palavra procurada
print(frase.find('curso'))
print(frase.lower().find('curso'))

###         Para separar as palavras da frase:            ###
print(frase.split())
frase_dividida = frase.split()
print(frase_dividida)
print(frase_dividida[0])
print(frase_dividida[2])
# Para mostrar uma letra dentro de uma posição de frase_dividida:
print(frase_dividida[2][2])

###          Usa-se tres ('') ara printar um testo grande:          ###
print('''Python é uma linguagem de programação criada por Guido van Rossum em 1991. Os objetivos do projeto da linguagem eram: produtividade e legibilidade. Em outras palavras, Python é uma linguagem que foi criada para produzir código bom e fácil de manter de maneira rápida. Além disso, Python suporta múltiplos paradigmas de programação. A programação procedimental pode ser usada para programas simples e rápidos, mas estruturas de dados complexas, como tuplas, listas e dicionários, estão disponíveis para facilitar o desenvolvimento de algoritmos complexos. Grandes projetos podem ser feitos usando técnicas de orientação a objetos, que é completamente suportada em Python (inclusive sobrecarga de operadores e herança múltipla). Um suporte modesto para programação funcional existe, o que torna a linguagem extremamente expressiva: é fácil fazer muita coisa com poucas linhas de comando. E também possui inúmeras capacidades de meta-programação: técnicas simples para alterar o comportamento de comportamentos da linguagem, permitindo a criação de linguagens de domínio específico.

Python tem uma biblioteca padrão imensa, que contém classes, métodos e funções para realizar essencialmente qualquer tarefa, desde acesso a bancos de dados a interfaces gráficas com o usuário. E, logicamente, já que esse é o objetivo deste grupo, existem muitas ferramentas para lidar com dados científicos. Essa característica da linguagem é comumente chamado baterias inclusas, significando que tudo que você precisa para rodar um programa está — na maior parte das vezes — presente na instalação básica.

Por fim, e não menos importante, Python é uma linguagem livre e multiplataforma. Isso significa que os programas escritos em uma plataforma serão executados sem nenhum problema na maioria das plataformas existentes sem nenhuma modificação. E, caso a plataforma objetivo não tenha uma versão de Python, desenvolvedores têm a liberdade de estudar e modificar o código da linguagem para fazer com que ela rode onde quer que seja.''')

