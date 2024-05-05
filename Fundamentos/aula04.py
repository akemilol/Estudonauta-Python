# Operadores Aritméticos

numero = 5 + 2 == 10
print(numero)
# testar se uma coisa é igual a outra usa == retorna true ou false


n1 = 5 + 3 * 2
print(n1)

n2 = 3 * 5 + 4 ** 2
print(n2)

n3 = 3 * (5 + 4) ** 2
print(n3)

n4 = pow(4, 3)
print(n4)

n5 = 81**(4/3)
print(n5)

n6 = '\noi' * 4
print(n6)

nome = input('Qual o seu nome?')
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d}', end=' ')
print(f'Divisão inteira {di} e potencia {e}')
