# Ex 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

########################

valor = float(input('Qual o valor do produto? R$ '))

desconto = 0.05

print('O produto, com 5% de desconto, fica por R$ {:.2f}'.format((valor - (valor * desconto))))
