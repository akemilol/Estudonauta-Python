# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o valor do produto, por favor: '))
desconto = produto * 0.15
descontoAplicado = desconto - produto
print(f'Com desconto de 15% o valor do produto é R$ {descontoAplicado}')
