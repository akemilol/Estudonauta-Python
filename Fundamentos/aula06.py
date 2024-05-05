# Manipulação de Cadeia de textos

# Fatiamento
frase = ('Curso em video Python')
teste1 = frase[9:21:2]
teste2 = frase[9:13]
teste3 = frase[9:21]
teste4 = frase[:5]
teste4 = frase[9::3]

print(f"""
    {teste1}
    {teste2}
    {teste3}
    {teste4}
""")

# analise
# len = comprimento len(frase) "Qual comprimento da frase?"
teste5 = len(frase)
print(teste5)

# frase.count('o') mostra quantos o tem na frase
teste6 = frase.count('o')
print(teste6)

teste7 = teste6 = frase.count('o', 0, 13)
print(teste7)

# frase.find('deo')
teste8 = frase.find('deo')
print(teste8)

# frase.find('android') não termos uma string adroind para o find procurar então ele retorna -1
teste9 = frase.find('android')
print(teste9)

# operador in ele retorna true or false
teste10 = 'Curso' in frase
print(teste10)

# Transformação:
teste11 = frase.replace('Python', 'Android')
print(teste11)

# frase.upper() deixa o texto contido em frase em maiusculo
teste12 = frase.upper()
print(teste12)

# frase.lower() deixa o texto contido em minusculo
teste13 = frase.lower()
print(teste13)

# frase.capitalize() coloca tudo em minusculo e deixa só a primeira letra da string maiuscula
teste14 = frase.capitalize()
print(teste14)


# frase.title() a cada espaço a primeira letra fica em maiusculo
teste15 = frase.title()
print(teste15)

texto = ('   Aprenda Python  ')
print(texto)

# texto.strip() remove os espaõs do começo e do fim
texto1 = texto.strip()
print(texto1)

# frase.rstrip() remove os ultimos espaços
texto2 = texto.rstrip()
print(texto2)

# frase.lstrip() remove os primeiros espaços
texto3 = texto.lstrip()
print(texto3)

# divisão

# frase.split() gera uma lista com todas palavras de uma string
teste16 = frase.split()
print(teste16)

# coloca - entre as p-a-l-a-v-r-a-s
teste17 = '-'.join(frase)
print(teste17)
