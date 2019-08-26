# Ex 010: Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

##############################################

dinheiro = float(input('Quantos reais você possui? R$ '))

dolar = 4.01     # Valor do dólar em reais no dia 17/08/2019

print('Você pode comprar US$ {:.2f} doláres.'.format(dinheiro / dolar))

