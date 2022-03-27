#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:13:54 2022

@author: cafe
"""

import csv


respostas = "Filme favorito.csv"

titulos = []
categorias = {}
with open(respostas) as arquivo:
    csv_reader = csv.DictReader(arquivo, delimiter=',')
    for linha in csv_reader:
        for categoria in linha["Categoria"].split(sep=";"):
            if categoria not in categorias:
                categorias[categoria] = 1
            else:
                categorias[categoria] += 1
        if linha["Título"].upper() not in titulos:
            titulos.append(linha["Título"].upper())
            # categorias.append(linha["Categoria"].split(sep=';'))
print(sorted(titulos))

# Análise
print(f"Foram enviados {len(titulos)} filmes")