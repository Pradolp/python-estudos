# Aula 01 - Exemplos: variáveis, tipos, print e input
# Rode com: python aula01/exemplos.py


# --- Criando variáveis -------------------------------------------------------
# %% Variaveis
nome = "Ana"
idade = 25
altura = 1.68
estudante = True
apelido = None  # ainda não tem apelido

# %% teste
print("=== Variáveis ===")
print(nome)
print(idade)
print(altura)
print(estudante)
print(apelido)

# --- Vendo o tipo de cada uma ------------------------------------------------
print("\n=== Tipos ===")  # \n pula uma linha
print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudante))
print(type(apelido))

# Cuidado: entre aspas é texto, mesmo que pareça número
print(type("25"))

# --- Atualizando uma variável ------------------------------------------------
print("\n=== Atualizando ===")
pontos = 10
print("Pontos no início:", pontos)
pontos = pontos + 5
print("Depois de ganhar 5:", pontos)
pontos += 3  # atalho para: pontos = pontos + 3
print("Depois de ganhar mais 3:", pontos)

# --- Formas de usar o print --------------------------------------------------
print("\n=== Formatação ===")
print("Nome:", nome, "| Idade:", idade)          # vírgulas
print("Nome: " + nome + " | Idade: " + str(idade))  # + só junta textos, por isso str()
print(f"Nome: {nome} | Idade: {idade}")          # f-string (a mais usada)

preco = 1234.5678
print(f"Preço com 2 casas: {preco:.2f}")
print(f"No ano que vem {nome} terá {idade + 1} anos")  # dá para fazer contas dentro das {}

# --- Conversões --------------------------------------------------------------
print("\n=== Conversões ===")
texto = "42"
numero = int(texto)
print(texto + texto)    # junta textos: 4242
print(numero + numero)  # soma números: 84

print(float("3.5"))   # 3.5
print(int(3.99))      # 3  (int corta a parte decimal, não arredonda)
print(round(3.99))    # 4  (round arredonda)
print(str(100) + "%")

print(bool(0), bool(1), bool(""), bool("oi"))  # zero e texto vazio são False

# --- input (descomente para testar) ------------------------------------------
# input() pausa o programa e espera você digitar algo e apertar Enter.
#
# cidade = input("Em que cidade você mora? ")
# ano = int(input("Em que ano você nasceu? "))
# print(f"Você mora em {cidade} e fará {2026 - ano} anos em 2026.")

# %%
