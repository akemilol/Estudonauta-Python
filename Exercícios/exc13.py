# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do seu salário atual: '))
aumento = salario * 0.15
aumentoAplicado = salario + aumento
print(f'Seu novo salário é R${aumentoAplicado}')
