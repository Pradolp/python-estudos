# Aula 03 - Exemplos: if, elif, else
# Rode com: python aula03/exemplos.py
# Mude os valores das variáveis e rode de novo para ver os outros caminhos.

print("=== if / else ===")
temperatura = 31
if temperatura > 30:
    print(f"{temperatura}°C: está calor, beba água.")
else:
    print(f"{temperatura}°C: temperatura agradável.")

print("\n=== if / elif / else ===")
nota = 6.8
if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
elif nota >= 5:
    conceito = "C"
else:
    conceito = "D"
print(f"Nota {nota} = conceito {conceito}")

print("\n=== Condições compostas ===")
idade = 17
if idade < 16:
    print("Não vota")
elif 16 <= idade < 18 or idade > 70:
    print("Voto opcional")
else:
    print("Voto obrigatório")

dia = "domingo"
if dia in ("sábado", "domingo"):
    print(f"{dia}: fim de semana")
else:
    print(f"{dia}: dia útil")

print("\n=== Aninhado ===")
usuario_cadastrado = True
senha_digitada = "1234"
senha_correta = "abcd"
if usuario_cadastrado:
    if senha_digitada == senha_correta:
        print("Login feito!")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")

print("\n=== Verdadeiro e falso ===")
nome = ""
if nome:
    print(f"Olá, {nome}")
else:
    print("Nome vazio conta como False")

print("\n=== Expressão condicional ===")
numero = 7
tipo = "par" if numero % 2 == 0 else "ímpar"
print(f"{numero} é {tipo}")

print("\n=== match ===")
opcao = "2"
match opcao:
    case "1":
        print("Você escolheu somar")
    case "2":
        print("Você escolheu subtrair")
    case _:
        print("Opção inválida")
