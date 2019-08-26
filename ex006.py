# Ex 006 - Faça um programa que leia um número
# e mostre na tela o seu dobro, triplo e raíz quadrada.

#################################################
num = float(input('Digite um número: '))

dobro = 2 * num
triplo = 3 * num
sqrt = num ** (1/2)

print('O número digitado foi {}. Seu dobro é {}, seu triplo é {}, e sua raíz quadrada é {:.2f}.'
      .format(num, dobro, triplo,sqrt))

# A raíz quadrada pode ser calculada usando a função: pow
# Por exemplo: pow (num, (1/2))

