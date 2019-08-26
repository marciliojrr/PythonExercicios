# Ex 015 -  Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

###################################################

kmPercorridos = float(input('Quantos quilometros foram percorridos? KMs = '))
diasAlugado = int(input('Por quantos dias o carro ficou alugado? '))

custoKM = 0.15
custoDia = 60

valorTotal = (kmPercorridos * custoKM) + (diasAlugado * custoDia)

print('Valor total a pagar: R$ {:.2f}.'.format(valorTotal))
