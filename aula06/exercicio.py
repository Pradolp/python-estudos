# Aula 06 - Exercícios
# Rode com: python aula06/exercicio.py

# -----------------------------------------------------------------------------
# Exercício 1: Notas da turma
# Leia 5 notas e guarde numa lista. Mostre:
#   - todas as notas
#   - a média
#   - a maior e a menor nota
#   - quantas notas ficaram acima da média
# Escreva seu código aqui:
#%%
notas = []
for i in range(5):
    nota = float(input("Digite sua nota:"))
    notas.append(nota)

media = sum(notas)/ len(notas)
print(f"Notas: {notas}")
print(f"Media: {media}")
print(f"Menor Nota: {min(notas)}, maior: {max(notas)}")
print(f"Notas acima da média: {[nota for nota in notas if nota >= media]}")


# -----------------------------------------------------------------------------
# Exercício 2: Pares e ímpares
# Leia 7 números inteiros. Separe em duas listas, uma de pares e outra de
# ímpares, e mostre as duas ordenadas.
# Escreva seu código aqui:
#%%
pares = []
impares = []
for i in range(7):
    num = int(input(f"Digite o {i+1} numero"))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"pares > {sorted(pares)}")
print(f"impares > {sorted(impares)}")



# -----------------------------------------------------------------------------
# Exercício 3: Sem repetidos
# Dada a lista abaixo, crie uma nova lista sem os valores repetidos,
# MANTENDO a ordem em que eles aparecem pela primeira vez.
#   Resultado esperado: [3, 1, 4, 5, 9, 2, 6]
#%%
valores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Escreva seu código aqui:
lista = []
for i in valores:
    if i not in lista:
        lista.append(i)

print(lista)

# -----------------------------------------------------------------------------
# Exercício 5: List comprehension
# Usando list comprehension, crie:
#   a) os cubos dos números de 1 a 10
#%%
#   b) as palavras da frase abaixo que têm mais de 4 letras
frase = "o python é uma linguagem muito usada em inteligência artificial"
# Escreva seu código aqui:
numeros_cubicos = [num**3 for num in range(1,11)]
palavras_longas = [palavra for palavra in frase.split() if len(palavra) > 4]
print(palavras_longas)
print(numeros_cubicos)


# %%
