# Ex 005 - Faça um programa que leia um número
# e mostre na tela seu antecessor e seu sucessor.

#################################################

num = int(input('Digite um número inteiro: '))

anterior = num - 1
sucessor = num + 1

print('O número digitado foi {}.\n'
      'Seu antecessor é {}'
      ' e seu sucessor é {}.'.format(num, anterior,sucessor))

# Para usar apenas a variável "num" no programa, podemos fazer o seguinte:
# print('O número digitado foi {}. Seu antecessor é {} e seu sucessor é {}.'.format(num, (num-1), (num+1)))



