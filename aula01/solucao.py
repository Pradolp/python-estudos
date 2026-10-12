# Aula 01 - Solução (abra só depois de tentar!)

# Exercício 1
nome = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
cidade = input("Cidade: ")
idade = 2026 - ano_nascimento
print(f"Olá, {nome}! Você é de {cidade} e faz {idade} anos em 2026.")

# Exercício 2
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura * altura)
print(f"Seu IMC é {imc:.2f}")

# Exercício 3
celsius = float(input("Temperatura em °C: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} °C = {fahrenheit} °F")

# Exercício 4
a = 7 / 2        # float 3.5   -> / sempre dá decimal
b = 7 // 2       # int 3       -> // é divisão inteira
c = "7" + "2"    # str "72"    -> + entre textos junta
d = int("7") + 2 # int 9
e = 3 > 2        # bool True
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
