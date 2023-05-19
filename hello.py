#!/usr/bin/env python3
""""Hello Word Multi Linguagem

Exibe a mensagem Hello World na linguagem definida no sistema pela variável
de ambiente LANG.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

import os

__version__ = "0.0.1"
__author__ = "Icaro Werly"
__license__ = "Unlicense"

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
	msg = "Olá, Mundo!"
elif current_language == "it_IT":
	msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
	msg = "Bonjour, Monde!"
	
print(msg)