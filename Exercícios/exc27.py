# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome_completo = input('Digite seu nome completo: ')

partes_nome = nome_completo.split()

primeiro_nome = partes_nome[0]
ultimo_nome = partes_nome[-1] 

print(f"""
    Nome Completo: {nome_completo}
    Primeiro nome: {primeiro_nome}
    Último nome: {ultimo_nome}
""")