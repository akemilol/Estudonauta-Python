# Crie um programa que leia o nome de uma  PESSOA e diga se ela tem "Silva" no nome

nome = input('Digite o nome da pessoa: ')

if "silva" in nome.lower():
    print('O nome contém Silva.')
else:
    print('O nome NÃO contém Silva.')