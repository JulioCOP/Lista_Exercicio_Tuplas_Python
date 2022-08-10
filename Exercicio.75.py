# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

n1=int(input("Digite um número: "))
n2=int(input("Digite mais um número: "))
n3=int(input("Outro número: "))
n4=int(input("Digite o último número: "))

total_numeros= (n1,n2,n3,n4)
print("O usuário digitou os seguintes números: ")
print()
print(total_numeros)
print(f"O número 9 apareceu em {total_numeros.count(9)} oportunidade(s)")
print()
if 3 in total_numeros:
    print(f"O valor 3 apareceu na {total_numeros.index(3)+1}º posição")
else:
    print("VALOR 3 NÃO ENCONTRADO")
print()
print("VALOR(ES) PAR(ES): ")
for numero in total_numeros:
    if numero%2==0:
        print(numero, end=" ")
    else:
        print("Dentre o valores informados, nenhum é par.")
    break
print()
print("FIM DO PROGRAMA")