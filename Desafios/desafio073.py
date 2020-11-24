# Este programa exibe a lista dos 17 primeiros colocados do campeonato brasoleiro
# E seguida exibe os cinco primeiros colocados, os 4 ultimos, todos em ordem alfabética, em que posição está a Bahia
times = ('Athletico-PR','Atlético-GO','Atlético-MG','Bahia','Botafogo','Bragantino',
         'Ceará','Corinthians','Coritiba','Flamengo','Fluminense','Fortaleza','Goiás',
         'Grêmio','Internacional','Palmeiras','Santos')
print('=-='*20)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=-='*20)
print(f'Os quatro ultimos colocados são: {times[-4:]}')
print('=-='*20)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('=-='*20)
print(f'O time do Bahia está na posição: {times.index("Bahia")+1}')
print('=-='*20)
