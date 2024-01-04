#!/usr/bin/env python3
"""Sistema de tabuada

Gera a tabuada de 1 a 10.
"""

__version__ = "0.0.1"
__author__ = "Icaro Werly"
__license__ = "Unlicense"

numeros = list(range(1, 11))

print(numeros)

for numero in numeros:
    print(f"Tabuada do {numero}:")
    for multiplicador in numeros:
        print(numero * multiplicador)
    print("----------------")