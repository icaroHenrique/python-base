#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Listar alunos em cada atividade por sala
# CONTINUE O CÓDIGO AQUI

lista_atividades = {
    "Ingles": aula_ingles,
    "Musica": aula_musica,
    "Dança": aula_danca
}

for nome_atividade, alunos in lista_atividades.items():
    print(f"Aula de {nome_atividade}!\n")
    
    atividade_sala1 = set(sala1).intersection(alunos)
    atividade_sala2 = set(sala2).intersection(alunos)

    print("Sala 1: ", atividade_sala1)
    print("Sala 2: ", atividade_sala2)
    print()
    print("-" * 30)
    print()