# Faça um programa que leia um número Inteiro e mostre na tela seu sucessor e antecessor

numero = int(input('Digite um número: '))
numeroAntecessor = numero - 1
numeroSucessor = numero + 1
print(f'o antecessor de {numero} é {
    numeroAntecessor} e seu sucessor é {numeroSucessor}')

# Crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada
n1 = int(input('Diga um número: '))
dobro = n1 * 2
triplo = n1 * 3
raizQuadrada = n1 ** 2
print(f'o dobro de {n1} é {dobro} seu triplo é {
    triplo} e a raiz quadrada é {raizQuadrada}')

# Desenvolva um programa que leia as duas notas de um aluno, calcule sua média.
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = nota1 / nota2 / 2
print(f'A media do aluno é {media}')

# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
tabuada = int(input('Digite um número para calcular a tabuada: '))
print(f'{tabuada} X 1 = {tabuada * 1}')
print(f'{tabuada} X 2 = {tabuada * 2}')
print(f'{tabuada} X 3 = {tabuada * 3}')
print(f'{tabuada} X 4 = {tabuada * 4}')
print(f'{tabuada} X 5 = {tabuada * 5}')
print(f'{tabuada} X 6 = {tabuada * 6}')
print(f'{tabuada} X 7 = {tabuada * 7}')
print(f'{tabuada} X 8 = {tabuada * 8}')
print(f'{tabuada} X 9 = {tabuada * 9}')
print(f'{tabuada} X 10 = {tabuada * 10}')

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar CONSIDERE US$1,00 = R$3,27
reais = float(input('Digite quanto dinheiro em reais você tem: '))
dolar = reais / 3.27
print(f'Com R${reais} você consegue comprar até US${dolar}')

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m2
altura = float(input('Por favor, digite a altura da parede: '))
largura = float(input('Por favor, digite a largura da parede: '))

area = altura * largura
qntDeTintaMetro = 1/2
qntDeTinta = area * qntDeTintaMetro

print(f'Você vai precisar de {
    qntDeTinta} tinta necessária, para a area da parede de {area}')

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o valor do produto, por favor: '))
desconto = produto * 0.15
descontoAplicado = desconto - produto
print(f'Com desconto de 15% o valor do produto é R$ {descontoAplicado}')

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do seu salário atual: '))
aumento = salario * 0.15
aumentoAplicado = salario + aumento
print(f'Seu novo salário é R${aumentoAplicado}')
