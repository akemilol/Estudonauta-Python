# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# o programa deverá escrever na tela se o usuario ghanhou ou perdeu

import random

numero = random.randint(0, 5)
tentativa = int(input("Tente adivinhar o número que o computador pensou (entre 0 e 5): "))

if tentativa == numero:
    print("Parabéns! Você acertou!")
else:
    print(f"Que pena! O número correto era {numero}. Tente novamente!")