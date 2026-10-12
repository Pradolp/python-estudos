# Aula 06 - Solução (abra só depois de tentar!)

# Exercício 1
notas = []
for i in range(1, 6):
    notas.append(float(input(f"Nota {i}: ")))
media = sum(notas) / len(notas)
acima = 0
for nota in notas:
    if nota > media:
        acima += 1
print("Notas:", notas)
print(f"Média: {media:.2f}")
print("Maior:", max(notas), "| Menor:", min(notas))
print("Acima da média:", acima)

# Exercício 2
pares = []
impares = []
for i in range(7):
    n = int(input(f"Número {i + 1}: "))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Pares:", sorted(pares))
print("Ímpares:", sorted(impares))

# Exercício 3
valores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sem_repetidos = []
for v in valores:
    if v not in sem_repetidos:
        sem_repetidos.append(v)
print(sem_repetidos)

# Exercício 4
compras = []
while True:
    print("\n[1] Adicionar  [2] Remover  [3] Ver lista  [0] Sair")
    opcao = input("Opção: ")
    if opcao == "0":
        break
    elif opcao == "1":
        compras.append(input("Item: ").strip())
    elif opcao == "2":
        item = input("Item a remover: ").strip()
        if item in compras:
            compras.remove(item)
        else:
            print(f"'{item}' não está na lista.")
    elif opcao == "3":
        if compras:
            for i, item in enumerate(compras, start=1):
                print(f"{i}. {item}")
        else:
            print("Lista vazia.")
    else:
        print("Opção inválida.")

# Exercício 5
frase = "o python é uma linguagem muito usada em inteligência artificial"
cubos = [n ** 3 for n in range(1, 11)]
longas = [p for p in frase.split() if len(p) > 4]
print("Cubos:", cubos)
print("Palavras longas:", longas)
