# Aula 05 - Solução (abra só depois de tentar!)

# Exercício 1
n = int(input("Tabuada de: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Exercício 2
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
if passo == 0:
    print("O passo não pode ser 0.")
else:
    for i in range(inicio, fim + (1 if passo > 0 else -1), passo):  # inclui o fim
        print(i, end=" ")
    print()

# Exercício 3
n = int(input("Fatorial de: "))
resultado = 1
conta = ""
for i in range(1, n + 1):
    resultado *= i
    conta += str(i) if i == 1 else f" x {i}"
print(f"{n}! = {conta} = {resultado}")

# Exercício 4
numero = int(input("Número: "))
primo = numero >= 2
for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = False
        break
print(f"{numero} {'é' if primo else 'não é'} primo")

# Exercício 5
frase = input("Frase: ").lower().replace(" ", "")
invertida = ""
for letra in frase:
    invertida = letra + invertida  # coloca cada letra NA FRENTE
if frase == invertida:
    print("É palíndromo!")
else:
    print("Não é palíndromo.")

# Exercício 6
altura = int(input("Altura: "))
for linha in range(1, altura + 1):
    for n in range(1, linha + 1):
        print(n, end=" ")
    print()
