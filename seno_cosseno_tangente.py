"""Faça um programa que leia um ângulo qualquer 
e mostre na tela o valor do seno,cosseno e tangente desse ângulo."""

import math
angulo = float(input("\nDigite o Angulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print ("\nO Seno é: {:.2f}".format(seno))
cosseno = math.cos(math.radians(angulo))
print ("\nO cosseno é: {:.2f}".format(cosseno))
tangente = math.tan(math.radians(angulo))
print ("\nO tangente é: {:.2f}".format(tangente))