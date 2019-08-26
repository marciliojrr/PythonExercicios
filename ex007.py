# Ex 007 - Faça um programa que leia duas notas de um aluno
# e calcule sua média

#################################################

n1 = float(input('Digita a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('A média do aluno, com notas {} e {} é {:.1f}.'.format(n1, n2, media))
