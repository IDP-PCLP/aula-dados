#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:13:54 2022

@author: cafe
"""

import csv

respostas = "Filme favorito.csv"

titulos = []
with open(respostas) as arquivo:
    csv_reader = csv.DictReader(arquivo, delimiter=',')
    for linha in csv_reader:
        titulos.append(linha["Título"].upper())
print(sorted(titulos))