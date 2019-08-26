# Ex 008 - Conversor de medidas
# Escreva um programa que leia um valor em metros
# e o exiba convertido em centimetros e milimetros.

###############################################

medida = (float(input('Digite o valor em metros: ')))

print('O valor digitado, em metros, foi {}m.\n'
      'Este valor é igual a:\n'
      '{} quilometros\n'
      '{:.0f} centimetros\n'
      '{:.0f} milimetros\n'
       .format(medida, medida / 1000, medida * 100, medida *1000))
