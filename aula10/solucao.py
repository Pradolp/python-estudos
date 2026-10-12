# Aula 10 - Solução (abra só depois de tentar!)
# O módulo do exercício 3 está em solucao_conversoes.py
import datetime
import math
import random

import solucao_conversoes as conv

# Exercício 1
alunos = [input(f"Aluno {i}: ") for i in range(1, 5)]
print("Vai apresentar:", random.choice(alunos))
ordem = alunos.copy()
random.shuffle(ordem)
print("Ordem de apresentação:", ordem)

# Exercício 2
dia = int(input("Dia em que nasceu: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
nascimento = datetime.date(ano, mes, dia)
dias = (datetime.date.today() - nascimento).days
print(f"Você tem {dias} dias de vida.")

# Exercício 3
c = float(input("Temperatura em °C: "))
print(f"{c} °C = {conv.celsius_para_fahrenheit(c):.1f} °F")
km = float(input("Distância em km: "))
print(f"{km} km = {conv.km_para_milhas(km):.2f} milhas")
reais = float(input("Valor em R$: "))
print(f"R$ {reais:.2f} = US$ {conv.reais_para_dolar(reais, 5.40):.2f} (cotação 5,40)")

# Exercício 4
# Em ferramentas/numeros.py:
#     def fatorial(n):
#         resultado = 1
#         for i in range(2, n + 1):
#             resultado *= i
#         return resultado
# Em ferramentas/__init__.py, troque a linha do import por:
#     from .numeros import eh_par, fatorial, media
# Aqui: from ferramentas import fatorial
print("5! =", math.factorial(5), "(a biblioteca padrão também tem: math.factorial)")
