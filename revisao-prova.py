#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:17:41 2022

@author: mac-prof
"""

# Tipos de dados
# Listas
minha_lista = ["eu","amo","Python"]
print(minha_lista[0])
print(minha_lista[1])
print(minha_lista[2])
minha_lista[2] = "Software Livre"
minha_lista.append("e desenho animado!")
print(minha_lista)
# Dicionários
aluno = {"curso":"Economia",0:1}
aluno["nome"] = "Xerxes"
print(aluno["nome"])
print(aluno["curso"])

# Controle de fluxo
clientes = ["IDP",'Google','Power Rangers']

print(f"Olá, {clientes[0]}")
print(clientes[1])
print(clientes[2])

for cliente in clientes:
    print(f"Olá, {cliente}")
    print("Dentro do bloco for")
print("Fora do bloco for")

executar = True
while executar == True:
    executar = False
    print("AAAAAAAHHHHH")

jogador = "Impar"
adversario = "Impar"
resultado = "Impar"

if jogador == adversario:
    print("Empatou!")
elif jogador == resultado:
    print("O jogador venceu!")
else:
    print("O adversario venceu...")

# Pandas e DataFrames
import pandas as pd

dados = pd.read_excel("pokemon_data.xlsx")

# Indexando um DataFrame
# Indexando uma coluna
print(dados["Name"]) 
# Acessando elementos de uma coluna
print(dados["Name"][0:10]) 
# Acessando utilizando .loc[linha,coluna]
print(dados.loc[0,"Name"])
# Acessando utilizando o .iloc[linha,coluna]
print(dados.iloc[0,1])

# Quantos pokemons existem?
print(dados.count())
print(dados["#"].max())

# Quantos pokemons possuem a letra "c" no nome?
iterador = 0
for nome in dados["Name"]:
    if "c" in nome:
        iterador = iterador + 1

print(f"{iterador} pokemons possuem 'c' no nome")

# Indexando por operações de comparação
pokemon = dados[dados["Name"] == "Bulbasaur"]
print(pokemon)

# Quais pokemons tem ataque acima de 100?
pokemon = dados[
    dados["Attack"] > 100].sort_values("Attack"
                                       ,ascending=False)
print(f"{pokemon['Name'].count()} pokemons tem ataque maior que cem")

# Quantos pokemons se repetem e quais são?

duplicados = dados[dados["#"].duplicated()]
print(duplicados["#"].count())
print(duplicados["Name"])

# Estatística descritiva

descricao = dados.describe()

agrupados = dados.groupby("Type 1").describe()




























