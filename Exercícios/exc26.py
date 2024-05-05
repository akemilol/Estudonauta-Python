# faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')

quantidade_a = frase.lower().count('a')

primeira_ocorrencia = frase.lower().find('a') + 1  
ultima_ocorrencia = frase.lower().rfind('a') + 1  

print(f"""
Quantidade de vezes que 'A' aparece na frase: {quantidade_a}
Posição da primeira ocorrência de 'A': {primeira_ocorrencia}
Posição da última ocorrência de 'A': {ultima_ocorrencia}
""")