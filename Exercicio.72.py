# Programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. O programa deverá lê o um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso, ao fim ele questiona ao usuário se o mesmo tem a intenção de
# continuar, ao optar por encerrar é mostrado quantos valores foram transformados.

cont=('zero','um','dois', 'três', 'quatro', 'cinco',
      'seis', 'sete', 'oito', 'nove', 'dez',
      'onze', 'doze', 'treze', 'quatorze','quinze',
      'dezesseis', 'dezessete', 'dezoito', 'dezenovo','vinte')
qtd_num=0
while True:
    n=int(input("Digite um número de 0 a 20: "))
    if n>20 or n<0:
        print("ERRO. VOCÊ DIGITOU UM NÚMERO FORA DO INTERVALO CORRESPONDENTE !")
        n=int(input("Digite novamente um número: "))
    qtd_num+=1

    print(f"Você digitou o número: {cont[n]}")

    resp=str(input("Usuário você deseja continuar ? [S] / [N] ")).strip().upper()[0]
    if resp=='N':
        break
print(f"Foram transformado por extenso {qtd_num} valores")

