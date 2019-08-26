# Ex 004 - Faça um programa que leia algo do teclado
# e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.
#################################################


user = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(user))
print('Só tem espaços? ', user.isspace())
print('É um número? ', user.isnumeric())
print('É alfabético? ', user.isalpha())
print('É alfanumérico? ', user.isalnum())
print('Está em maiúsculas? ', user.isupper())
print('Está em minúsculas? ', user.islower())
print('Está capitalizada? ', user.istitle())
