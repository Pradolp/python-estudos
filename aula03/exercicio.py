# Aula 03 - Exercícios
# Rode com: python aula03/exercicio.py

# -----------------------------------------------------------------------------
# Exercício 1: Par ou ímpar
# Leia um número inteiro e diga se ele é par ou ímpar.
# Escreva seu código aqui:
#%%
numero = int(input("Numero:"))
tipo  = "par" if numero % 2 == 0 else "impar"
print(f"Numero é: {tipo}")

# -----------------------------------------------------------------------------
# Exercício 2: Boletim
# Leia duas notas, calcule a média e mostre:
#   média >= 7          -> "Aprovado"
#   5 <= média < 7      -> "Recuperação"
#   média < 5           -> "Reprovado"
# Escreva seu código aqui:



# -----------------------------------------------------------------------------
# Exercício 3: Ano bissexto
# Leia um ano e diga se ele é bissexto. Regra:
#   é divisível por 4 E não é divisível por 100,
#   OU é divisível por 400.
# Teste: 2024 (sim), 1900 (não), 2000 (sim), 2026 (não)
# Escreva seu código aqui:
#%%
ano = int(input("Ano:"))
if ano % 400 == 0: 
    print("Sim")
else:
    print("Não")

# -----------------------------------------------------------------------------
# Exercício 4: O maior de três
# Leia três números e mostre o maior deles SEM usar a função max().
# Escreva seu código aqui:



# -----------------------------------------------------------------------------
# Exercício 5: Multa por velocidade
# Leia a velocidade de um carro. Se passar de 80 km/h, mostre que foi multado.
# A multa é R$ 7,00 por km acima do limite.
#   Velocidade: 95 -> Multado! Valor: R$ 105.00
# Escreva seu código aqui:



# %%
