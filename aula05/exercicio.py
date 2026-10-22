# Aula 05 - Exercícios (use for em todos)
# Rode com: python aula05/exercicio.py

# -----------------------------------------------------------------------------
# Exercício 1: Tabuada
# Leia um número e mostre a tabuada dele de 1 a 10.
# Escreva seu código aqui:
#%%
numero = int(input("Digite um numero inteiro"))
for i in range(1, 11):
    print(f"{numero} * {i:2} = {numero * i:2}")


# -----------------------------------------------------------------------------
# Exercício 2: Contagem personalizada
# Leia o início, o fim e o passo, e mostre a contagem usando range.
# Bônus: se o passo for 0, mostre um aviso (range não aceita passo 0).
# Escreva seu código aqui:
#%%
inicio = int(input("Valor de inicio da contagem"))
fim = int(input("Valor de fim da contagem"))
passo = int(input("Valor do passo que deve ser contado"))
for i in range(inicio, fim, passo):
    print(i, end=" ")

    

# -----------------------------------------------------------------------------
# Exercício 3: Fatorial
# Leia um número inteiro n e calcule n! = 1 x 2 x 3 x ... x n
# Mostre a conta completa:  5! = 1 x 2 x 3 x 4 x 5 = 120
# Escreva seu código aqui:
#%%
numero = int(input("Numero:"))
contador = 1
conta = ""
for i in range(1, numero + 1):
    contador *= i
    conta += str(i) if i == 1 else f" x {i}"
print(f"{numero}! = {conta} = {contador}")


# -----------------------------------------------------------------------------
# Exercício 4: Número primo
# Leia um número e diga se ele é primo (só é divisível por 1 e por ele mesmo).
# Lembre: 0 e 1 não são primos.
# Escreva seu código aqui:



# -----------------------------------------------------------------------------
# Exercício 5: Palíndromo
# Leia uma frase e diga se ela é um palíndromo (lida igual de trás para frente),
# ignorando espaços. Exemplos: "arara", "a sacada da casa".
# Faça usando for (sem usar o atalho [::-1]).
# Escreva seu código aqui:



# -----------------------------------------------------------------------------
# Exercício 6: Pirâmide de números
# Leia a altura e desenhe:
#   1
#   1 2
#   1 2 3
#   1 2 3 4
# Escreva seu código aqui:



# %%
