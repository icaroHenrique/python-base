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
__version__ = "0.0.1"
__author__ = "Icaro Werly"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
	"en_US": "Hello, World!",
	"pt_BR": "Olá, Mundo!",
	"it_IT": "Ciao, Mondo!",
	"fr_FR": "Bonjour, Monde!"
}
	
print(msg[current_language])