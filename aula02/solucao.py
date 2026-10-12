# Aula 02 - Solução (abra só depois de tentar!)

# Exercício 1
n = int(input("Digite um número: "))
print(f"Antecessor: {n - 1}")
print(f"Sucessor: {n + 1}")
print(f"Dobro: {n * 2} | Triplo: {n * 3}")
print(f"Raiz quadrada: {n ** 0.5:.2f}")

# Exercício 2
numero = int(input("Número de 0 a 9999: "))
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f"Unidade: {unidade} | Dezena: {dezena} | Centena: {centena} | Milhar: {milhar}")

# Exercício 3
nome = input("Nome completo: ").strip()
print("Maiúsculas:", nome.upper())
print("Minúsculas:", nome.lower())
print("Letras (sem espaços):", len(nome.replace(" ", "")))
print("Primeiro nome:", nome.split()[0])
print("Tem Silva?", "silva" in nome.lower())  # lower() para aceitar SILVA, silva...

# Exercício 4
preco = float(input("Preço: R$ "))
novo = preco - preco * 5 / 100  # ou: preco * 0.95
print(f"Com 5% de desconto: R$ {novo:.2f}")
