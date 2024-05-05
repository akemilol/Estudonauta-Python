# Escreva um programa que pergunte o salário de um funcionario e calcule o valor do aumento.

# para salarios superiores a R$1.250,00 calcule um aumento de 10%

# para inferiores ou iguais o aumento é de 15%


salario = float(input("Digite o salário do funcionário: "))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15


novo_salario = salario + aumento

print(f"O valor do aumento é R${aumento:.2f}.")
print(f"O novo salário é R${novo_salario:.2f}.")