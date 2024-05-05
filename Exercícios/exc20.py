# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatros alunos e motre na ordem sorteada
import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print('Ordem de apresentação dos alunos:')
for i, aluno in enumerate(alunos, start=1):
    print(f'{i}. {aluno}')


# A função random.shuffle() embaralha os elementos de uma lista de forma aleatória.
