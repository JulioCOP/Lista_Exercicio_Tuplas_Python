#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
#mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

n=(randint(0,500), randint(0,500), randint(0,500), randint(0,500), randint(0,500))
print("Os valores sorteados foram: ")
for c in n:
    print(f"{c}", end=" ")
print()
print(f"\nO maior valor sorteado \033[1;31m{max(n)}\033[m")
print(f"\nE o menor valor sorteado foi \033[1;35m{min(n)}\033[m")
