# Crie um programa que leia o nome completo de uma pessoa e mostre: nome com todas lestras maiusculas, o nome com todas minúsculas quantas letras ao todos sem espaços quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')

nome_caixa_alta = nome.upper()
nome_caixa_baixa = nome.lower()
quantidade_letras = len(nome.replace(" ", ""))
primeiro_nome = nome.split()[0]
primeiro_nome = len(primeiro_nome)
print(f"""
    {nome_caixa_alta}
    {nome_caixa_baixa}
    {quantidade_letras}
    {primeiro_nome}
    """)
