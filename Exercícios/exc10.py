# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar CONSIDERE US$1,00 = R$3,27
reais = float(input('Digite quanto dinheiro em reais você tem: '))
dolar = reais / 3.27
print(f'Com R${reais} você consegue comprar até US${dolar}')
