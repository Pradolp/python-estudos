# Aula 02 - Exercícios
# Rode com: python aula02/exercicio.py

# -----------------------------------------------------------------------------
# Exercício 1: Raio-X de um número
# Leia um número inteiro e mostre: o antecessor, o sucessor, o dobro,
# o triplo e a raiz quadrada (com 2 casas).
# Escreva seu código aqui:
# %% 
numero = int(input("Digite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5
print(f"Antecessor: {antecessor}")
print(f"Sucessor: {sucessor}")
print(f"Dobro: {dobro}")
print(f"Triplo: {triplo}")
print(f"Raiz quadrada: {raiz_quadrada:.2f}")

# -----------------------------------------------------------------------------
# Exercício 2: Separando dígitos
# Leia um número de 0 a 9999 e mostre cada dígito separado, usando // e %.
#   Número: 1834
#   Unidade: 4 | Dezena: 3 | Centena: 8 | Milhar: 1
# Dica: 1834 % 10 = 4 e 1834 // 10 % 10 = 3
# Escreva seu código aqui:
# %%
numero = int(input("Digite um número de 0 a 9999: "))
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f"Unidade: {unidade} | Dezena: {dezena} | Centena: {centena} | Milhar: {milhar}") 

# -----------------------------------------------------------------------------
# Exercício 3: Analisando um nome
# Leia o nome completo de uma pessoa e mostre:
#   - o nome todo em maiúsculas e em minúsculas
#   - quantas letras tem, sem contar os espaços
#   - o primeiro nome
#   - se o nome contém "Silva" (True/False)
# Escreva seu código aqui:
#%%
nome = "Lucas Silva do Prado"
nome_limpo = nome.replace(" ", "")
primeiro_nome = nome.split()[0]

print(f"Nome em maiúsculas: {nome.upper()}")
print(f"Quantidade de letras (sem espaços): {len(nome_limpo)}")
print(f"Primeiro nome: {primeiro_nome}")
print(f"Contém 'Silva': {'Silva' in nome}")

# -----------------------------------------------------------------------------
# Exercício 4: Desconto
# Leia o preço de um produto e mostre o novo preço com 5% de desconto,
# formatado com 2 casas decimais.
# Escreva seu código aqui:
#%%
preco = float(input("Digite o preço do produto: R$ "))
novo_preco = preco * 0.95
print(f"Preço com desconto: R$ {novo_preco:.2f}")



# %%
