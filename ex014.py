# Ex 015 - Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.
###############################

tempC = float(input('Digite a temperatura em graus Celsius: '))

CtoFah = (tempC * (9/5) + 32)

print('{:.1f}ºC equivale a {:.1f}ºF.'.format(tempC, CtoFah))
