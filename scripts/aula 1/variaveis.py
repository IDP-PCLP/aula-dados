#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:12:09 2022

@author: cafe
"""


# Variáveis em Python são declaradas com o sinal de =

numero = 1
texto = "Olá, mundo!"
booleano = True # ou False

# Podemos atribuir resultados de funções a variáveis
nome = input("Qual é seu nome? ")
print(f"Olá, {nome}!")
# Listas e dicionários

nomes = ["Álvaro", "Bernardo", "Beatriz"]

nomes[0] # Acessando elementos de uma lista
for nome in nomes:
    print(nome)


alunos = {"Álvaro":0, "Bernardo":1, "Beatriz":2}

for id,nome in enumerate(alunos):
    print(nome,id)