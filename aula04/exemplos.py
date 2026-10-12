# Aula 04 - Exemplos: while
# Rode com: python aula04/exemplos.py

print("=== Contador ===")
contador = 1
while contador <= 5:
    print("Volta", contador)
    contador += 1
print("Valor do contador ao sair:", contador)  # 6: foi o valor que deixou a condição falsa

print("\n=== Contagem regressiva ===")
n = 5
while n > 0:
    print(n, end=" ")  # end=" " troca a quebra de linha por espaço
    n -= 1
print("Fogo!")

print("\n=== Acumulador: soma de 1 a 100 ===")
soma = 0
i = 1
while i <= 100:
    soma += i
    i += 1
print("Soma:", soma)

print("\n=== Sentinela (com dados simulados) ===")
# No programa real os números viriam do input(). Aqui uma lista simula o que foi digitado.
digitados = [8, 3, 10, 0]
posicao = 0
total = 0
quantidade = 0
numero = digitados[posicao]
while numero != 0:
    total += numero
    quantidade += 1
    posicao += 1
    numero = digitados[posicao]
print(f"{quantidade} números, soma {total}, média {total / quantidade:.2f}")

print("\n=== break ===")
n = 1
while True:
    if n * n > 50:
        print(f"O primeiro quadrado maior que 50 é {n}² = {n * n}")
        break
    n += 1

print("\n=== continue: ímpares de 1 a 10 ===")
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # pula os pares
    print(n, end=" ")
print()

print("\n=== Dobrando até passar de 1000 ===")
valor = 1
passos = 0
while valor <= 1000:
    valor *= 2
    passos += 1
print(f"Depois de {passos} dobras, o valor é {valor}")

# --- Menu interativo (descomente para testar) --------------------------------
# while True:
#     print("\n[1] Dizer olá  [2] Dizer tchau  [0] Sair")
#     opcao = input("Escolha: ")
#     if opcao == "0":
#         break
#     elif opcao == "1":
#         print("Olá!")
#     elif opcao == "2":
#         print("Tchau!")
#     else:
#         print("Opção inválida")
