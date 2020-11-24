# Este é um programa de teste para as cores do terminal
print('\033[1;34;40m Olá mundo! \033[m')

a = 3
b = 5
print(' Os valores são \033[4;31;40m{}\033[m e \033[1;30;41m{}\033[m !!!'.format(a,b))

nome = 'marcos'
print('Olá, muito praser em te conhacer {}{}{}'.format('\033[1;36;40m',nome,'\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá {}{}{}, muito prazer em te conhecer!!!'.format(cores['pretoebranco'],nome,cores['limpa']))
