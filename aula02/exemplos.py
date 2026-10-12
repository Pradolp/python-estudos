# Aula 02 - Exemplos: operadores e strings
# Rode com: python aula02/exemplos.py

print("=== Aritméticos ===")
a, b = 17, 5  # atribuição múltipla: a = 17 e b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}   (quantas vezes o 5 cabe no 17)")
print(f"{a} % {b} = {a % b}    (o que sobra)")
print(f"{a} ** 2 = {a ** 2}")
print("Raiz quadrada de 16:", 16 ** 0.5)

print("\nOrdem de precedência:")
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20

print("\nUso clássico do %:")
for numero in [10, 7]:  # (o for vem na aula 05; aqui ele só repete para 10 e 7)
    print(numero, "é par?", numero % 2 == 0)

segundos = 3725
horas = segundos // 3600
minutos = segundos % 3600 // 60
resto = segundos % 60
print(f"{segundos} segundos = {horas}h {minutos}min {resto}s")

print("\n=== Comparação e lógica ===")
idade = 20
tem_ingresso = False
print("Maior de idade?", idade >= 18)
print("Pode entrar? (and)", idade >= 18 and tem_ingresso)
print("Tem algum dos dois? (or)", idade >= 18 or tem_ingresso)
print("Não tem ingresso? (not)", not tem_ingresso)
print("Entre 18 e 30?", 18 <= idade <= 30)  # Python permite encadear comparações

print("\n=== Strings ===")
frase = "  Aprender Python é divertido  "
print(f"Original: [{frase}]")
limpa = frase.strip()
print(f"strip:    [{limpa}]")
print("upper:   ", limpa.upper())
print("lower:   ", limpa.lower())
print("replace: ", limpa.replace("divertido", "muito útil"))
print("count 'e':", limpa.lower().count("e"))
print("find 'Python':", limpa.find("Python"))
print("split:   ", limpa.split())
print("Tem 'Python'?", "Python" in limpa)
print("Tamanho:", len(limpa))

print("\n=== Índices e fatias ===")
s = "Python"
print("s[0] =", s[0])
print("s[-1] =", s[-1])
print("s[0:3] =", s[0:3])
print("s[2:] =", s[2:])
print("s[::-1] =", s[::-1])

print("\n=== Juntar e repetir ===")
print("=" * 30)
print("Py" + "thon")
nome_completo = "maria da silva"
print(nome_completo.title())
primeiro_nome = nome_completo.split()[0]
print("Primeiro nome:", primeiro_nome)
