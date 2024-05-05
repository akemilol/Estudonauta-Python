n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi {media:.1f}')

if media >= 8:
    print('Parabéns, você está entre os 10 melhores alunos!')
elif media >= 6:
    print('Você está na média, mas precisa melhorar!')
else:
    print('Você reprovou, consulte a diretoria para saber mais...')

