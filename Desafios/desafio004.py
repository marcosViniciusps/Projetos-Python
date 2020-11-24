#Este programa exibe varios tipos primitivos da informação fornecida pelo usuário
info = input('Digite algo: ')
print('É  um numero? ',info.isalnum())
print('É alpha? ',info.isalpha())
print('É maiúscula? ',info.isupper())
print('É minuscula? ',info.islower())
print('Está captalizada? ',info.istitle())

