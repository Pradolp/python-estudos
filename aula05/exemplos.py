# Aula 05 - Exemplos: for e range
# Rode com: python aula05/exemplos.py

print("=== Percorrendo uma string ===")
for letra in "Python":
    print(letra, end="-")
print()

print("\n=== range ===")
print("range(5):        ", list(range(5)))  # list() só para mostrar os números
print("range(1, 6):     ", list(range(1, 6)))
print("range(0, 11, 2): ", list(range(0, 11, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))

print("\n=== Tabuada do 7 ===")
for i in range(1, 11):
    print(f"7 x {i:2} = {7 * i:2}")  # :2 reserva 2 espaços e alinha a coluna

print("\n=== Acumulador: soma dos pares de 1 a 100 ===")
soma = 0
for n in range(2, 101, 2):
    soma += n
print("Soma:", soma)

print("\n=== Contando vogais ===")
frase = "Programar em Python é divertido"
vogais = 0
for letra in frase.lower():
    if letra in "aeiouáéíóúâêôãõ":
        vogais += 1
print(f'"{frase}" tem {vogais} vogais')

print("\n=== enumerate ===")
for numero, fruta in enumerate(["maçã", "banana", "uva"], start=1):
    print(f"{numero}. {fruta}")

print("\n=== Fatorial de 5 ===")
fatorial = 1
for n in range(1, 6):
    fatorial *= n
    print(f"Depois de multiplicar por {n}: {fatorial}")

print("\n=== for com else: 37 é primo? ===")
numero = 37
for divisor in range(2, numero):
    if numero % divisor == 0:
        print(f"{numero} não é primo (divisível por {divisor})")
        break
else:
    print(f"{numero} é primo")

print("\n=== Laços aninhados: triângulo ===")
for linha in range(1, 6):
    for _ in range(linha):
        print("*", end="")
    print()

print("\n=== Laços aninhados: mini tabela de multiplicação ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i * j:3}", end="")
    print()
