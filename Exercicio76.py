#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
#na sequência.No final, mostre uma listagem de preços, organizando os dados em forma tabular.

mercadoria= ('Livro', 47.70,
             'Computador', 5237.90,
             'Monitor', 800,
             'Caderno', 24.90,
             'Mesa Escritório', 239.80)
print()
print(f'{"LISTAGEM DE PREÇOS:":^40}')
print()
for pos in range(0,len(mercadoria)):
    if pos%2==0:
        print(f"{mercadoria[pos]:.<30}", end=" ")
    else:
        print(f"R$ {mercadoria[pos]:.>5.2f}")
