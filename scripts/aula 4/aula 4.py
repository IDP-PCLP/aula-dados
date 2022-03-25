#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:42:15 2022

@author: cafe
"""

nome = "Álvaro"
idade = 32
idade_em_dias = idade * 365.25
sede = True

# Estruturas de dados
# Listas
lista_de_nomes = ["Álvaro","Leticia","Maria","Sophia"]

# Laços for ou "para cada"

for name in lista_de_nomes:
    print(name)
    if name == "Álvaro":
        print("Oi, Álvaro")
    else:
        print("Olá, amigo")