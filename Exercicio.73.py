# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Atlético Mineiro.

time= ('Atlético Mineiro', 'América Mineiro', 'São Paulo', 'Santos', 'Palmeiras',
       'Corinthians', 'Fluminense', 'Flamengo', 'Juventude', 'Avai', 'Atlhetico Paranaense',
       'Coritiba', 'Ceará', 'Fortaleza', 'Internacioal', 'Cuiabá', 'Botafogo', 'RB Bragantino',
       'Atlético-GO', 'Goiás')
print(f"A classificação do Brasileirão é: ")
for t in time:
    print (f"{t}")
print("~"*124)
print(f"Os 5 primeiros colocados do campeonato: {time[0:5]}")
print("~"*124)
print(f"O Z4 do campenato é: {time[16:]}")
print("~"*124)
print(f'Os times em ordem alfabética:{sorted(time)}')
print("~"*124)
print(f"O \033[1;30mClube Atlético Mineiro\033[m está na "
      f"\033[1;33m{time.index('Atlético Mineiro')+1}ºposição\033[m")
