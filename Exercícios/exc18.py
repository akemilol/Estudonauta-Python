# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo

import math

angulo_grau = float(input('Digite o valor do ângulo em graus: '))
angulo_radianos = math.radians(angulo_grau)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f'''
    O seno do ângulo é: {seno}
    o cosseno do ângulo é: {cosseno}
    e a tangente do ângulo é: {tangente}
    ''')
