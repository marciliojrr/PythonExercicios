# Ex 017
# Faça um programa que leia o cateto oposto e o adjacente de um triângulo
# retângulo e calcule a hipotenusa.

from math import hypot
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))

hip = hypot(a,b)

print('A hipotenusa vale {:.2f}'.format(hip))



