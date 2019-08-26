# Ex 018
# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite o valor do ângulo: '))

print('O ângulo digitado foi {}.\n'
      'Seu seno vale {:.3f}.\n'
      'Seu cosseno vale {:.3f}.\n'
      'Sua tangente vale {:.3f}.'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))

