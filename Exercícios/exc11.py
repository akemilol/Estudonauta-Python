# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m2
altura = float(input('Por favor, digite a altura da parede: '))
largura = float(input('Por favor, digite a largura da parede: '))

area = altura * largura
qntDeTintaMetro = 1/2
qntDeTinta = area * qntDeTintaMetro

print(f'Você vai precisar de {
    qntDeTinta} tinta necessária, para a area da parede de {area}')
