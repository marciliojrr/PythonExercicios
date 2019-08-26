# Ex 016
# Crie um programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua porção inteira.

from math import trunc
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira igual a {}.'.format(num, trunc(num)))

# pode-se fazer o truncamento usando a função int(x)

