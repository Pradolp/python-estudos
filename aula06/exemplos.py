# Aula 06 - Exemplos: listas
# Rode com: python aula06/exemplos.py

print("=== Criando e acessando ===")
frutas = ["maçã", "banana", "uva", "laranja"]
print(frutas)
print("Primeira:", frutas[0])
print("Última:", frutas[-1])
print("Duas primeiras:", frutas[:2])
print("Quantidade:", len(frutas))
print("Tem uva?", "uva" in frutas)

print("\n=== Alterando ===")
frutas[1] = "manga"
print("Trocando banana por manga:", frutas)

print("\n=== Adicionando ===")
frutas.append("kiwi")
print("append('kiwi'):", frutas)
frutas.insert(0, "abacaxi")
print("insert(0, 'abacaxi'):", frutas)
frutas.extend(["pera", "melão"])
print("extend:", frutas)

print("\n=== Removendo ===")
frutas.remove("uva")
print("remove('uva'):", frutas)
ultima = frutas.pop()
print(f"pop() tirou '{ultima}':", frutas)
primeira = frutas.pop(0)
print(f"pop(0) tirou '{primeira}':", frutas)
del frutas[1]
print("del frutas[1]:", frutas)

print("\n=== Ordenando ===")
numeros = [42, 7, 19, 3, 88, 7]
print("Original:", numeros)
print("sorted() devolve nova:", sorted(numeros))
print("Original continua:", numeros)
numeros.sort()
print("Depois de .sort():", numeros)
numeros.sort(reverse=True)
print("reverse=True:", numeros)

print("\n=== Estatísticas ===")
notas = [7.5, 8.0, 6.5, 9.0, 10.0]
print("Notas:", notas)
print("Soma:", sum(notas))
print("Média:", sum(notas) / len(notas))
print("Menor:", min(notas), "| Maior:", max(notas))
print("Posição da maior:", notas.index(max(notas)))
print("Quantas vezes o 7 aparece em numeros:", numeros.count(7))

print("\n=== Percorrendo ===")
for i, nota in enumerate(notas, start=1):
    situacao = "ok" if nota >= 7 else "abaixo"
    print(f"Nota {i}: {nota} ({situacao})")

print("\n=== Filtrando com for + append ===")
aprovadas = []
for nota in notas:
    if nota >= 8:
        aprovadas.append(nota)
print("Notas >= 8:", aprovadas)

print("\n=== Mesma coisa com list comprehension ===")
print("Notas >= 8:", [nota for nota in notas if nota >= 8])
print("Quadrados:", [n * n for n in range(1, 6)])
print("Arredondadas:", [round(nota) for nota in notas])

print("\n=== Cópia x referência ===")
a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print("a:", a, "| b:", b, "| c:", c)

print("\n=== Matriz (lista de listas) ===")
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Elemento linha 1, coluna 2:", matriz[1][2])
for linha in matriz:
    for valor in linha:
        print(f"{valor:3}", end="")
    print()

print("\n=== split e join ===")
csv = "Ana,Bruno,Carla"
nomes = csv.split(",")
print("split:", nomes)
print("join:", " | ".join(nomes))
