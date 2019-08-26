# Ex 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#
######################################

salario = float(input('Digite o valor do salário: R$ '))

aumento = 0.15

print('O valor do salário com aumento de 15% é de R$ {:.2f}.'.format(salario + (salario * aumento)))
