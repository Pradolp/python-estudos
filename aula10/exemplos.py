# Aula 10 - Exemplos: módulos e pacotes
# Rode com: python aula10/exemplos.py
# (o Python procura os módulos importados na pasta do arquivo que está rodando,
#  por isso o pacote "ferramentas" é encontrado)

import datetime as dt
import json
import math
import os
import random
import sys
from pathlib import Path

from ferramentas import eh_par, media  # nomes reexportados pelo __init__.py
from ferramentas import textos  # o módulo inteiro
from ferramentas.textos import criar_slug as slug  # um nome, com apelido

print("=== math ===")
print("Raiz de 2:", math.sqrt(2))
print("Pi:", math.pi)
print("Arredondar para cima 2.1:", math.ceil(2.1))
print("Arredondar para baixo 2.9:", math.floor(2.9))

print("\n=== random ===")
random.seed(42)  # fixa a "sorte" para o resultado se repetir; tire para variar
print("Dado:", random.randint(1, 6))
print("Sorteio:", random.choice(["Ana", "Bruno", "Carla"]))
cartas = ["A", "K", "Q", "J"]
random.shuffle(cartas)
print("Embaralhado:", cartas)

print("\n=== datetime ===")
hoje = dt.date.today()
print("Hoje:", hoje)
print("Formatado:", hoje.strftime("%d/%m/%Y"))
natal = dt.date(hoje.year, 12, 25)
print("Dias até o Natal:", (natal - hoje).days)

print("\n=== json (o formato das APIs) ===")
dados = {"nome": "Ana", "linguagens": ["Python", "SQL"]}
texto_json = json.dumps(dados, ensure_ascii=False)
print("Dicionário -> JSON:", texto_json)
de_volta = json.loads(texto_json)
print("JSON -> dicionário:", de_volta["linguagens"])

print("\n=== os, sys e pathlib ===")
print("Versão do Python:", sys.version.split()[0])
print("Variável de ambiente HOME/USERPROFILE:", os.getenv("USERPROFILE") or os.getenv("HOME"))
print("Chave de API configurada?", os.getenv("GOOGLE_API_KEY") is not None)
pasta = Path(__file__).parent  # pasta onde este arquivo está
print("Arquivos .py nesta pasta:", [p.name for p in pasta.glob("*.py")])

print("\n=== Nosso pacote 'ferramentas' ===")
print("eh_par(10):", eh_par(10))
print("media([7, 8, 9]):", media([7, 8, 9]))
print("remover_acentos:", textos.remover_acentos("Inteligência Artificial é ótima"))
print("contar_palavras:", textos.contar_palavras("aprender python todo dia"))
print("criar_slug:", slug("Olá, Mundo! Minha 1ª Aula"))

print("\n=== __name__ ===")
print("Neste arquivo __name__ vale:", __name__)
print("No módulo importado vale:", textos.__name__)
