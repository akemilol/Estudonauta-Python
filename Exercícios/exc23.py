# faça um programa que leia o número de 0 a 9999 e mostre na tela cada um dos digitos separados

# exemplo: digite um número: unidade:4 dezena:3 centena:8 milhar:1

numero = int(input('Digite um número de 0 a 9999: '))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f"""
Número digitado: {numero}
Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}
""")
