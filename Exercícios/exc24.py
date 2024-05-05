# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nõo com o nome "SANTO"

cidade = input('Digite o nome da cidade: ')
cidade_minuscula = cidade.lower()

print(f"O nome da cidade {'começa' if cidade_minuscula.startswith('santo') else 'não começa'} com 'SANTO'.")