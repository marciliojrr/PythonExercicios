# Ex 011 -  Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
# uma área de 2 metros quadrados.

#################################

altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))

area = altura * largura

print('Sua parede tem {} m² de área. Para pinta-la precisa-se de {:.4} litros de tinta.'.format(area, (area / 2)))

