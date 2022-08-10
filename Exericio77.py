#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
#(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavra=('Ceu', 'Amor', 'Odio', 'Pequeno', 'Grande',
         'Breve', 'Desenvolvedor', 'Programacao', 'phyton'
         'Software', 'Tecnologia', 'Engenharia', 'Construcao', 'Casa',
         'Casa', 'Carro')
for p in palavra:
    print(f"\nPara cada palavra \033[1;31m{p.upper()}\033[m temos", end=" ")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;36m{letra}\033[m', end=" ")
