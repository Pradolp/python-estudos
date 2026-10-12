# Aula 07 - Solução (abra só depois de tentar!)

# Exercício 1
jogador = {"nome": input("Nome do jogador: "), "gols": []}
partidas = int(input("Quantas partidas? "))
for i in range(1, partidas + 1):
    jogador["gols"].append(int(input(f"Gols na partida {i}: ")))
jogador["total"] = sum(jogador["gols"])
print(jogador)
for i, gols in enumerate(jogador["gols"], start=1):
    print(f"Partida {i}: {gols} gols")

# Exercício 2
frase = input("Frase: ").lower()
letras = {}
for c in frase:
    if c != " ":
        letras[c] = letras.get(c, 0) + 1
for letra in sorted(letras):
    print(f"{letra}: {letras[letra]}")

# Exercício 3
pessoas = []
while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    pessoas.append({"nome": nome, "idade": idade})
    resposta = input("Quer continuar? [S/N] ").strip().upper()
    if resposta == "N":
        break
media = sum(p["idade"] for p in pessoas) / len(pessoas)
print(f"Cadastradas: {len(pessoas)}")
print(f"Média de idade: {media:.1f}")
print("Acima da média:", [p["nome"] for p in pessoas if p["idade"] > media])

# Exercício 4
estoque = {"caneta": 10, "caderno": 5, "borracha": 0}
produto = input("Produto: ").strip().lower()
if produto not in estoque:
    print("Produto não existe.")
else:
    quantidade = int(input("Quantidade: "))
    if quantidade > estoque[produto]:
        print(f"Só temos {estoque[produto]} unidade(s) de {produto}.")
    else:
        estoque[produto] -= quantidade
        print("Venda feita!")
print("Estoque:", estoque)

# Exercício 5
python = set(["Ana", "Bruno", "Carla", "Diego", "Ana"])
ingles = set(["Carla", "Eva", "Bruno", "Fábio"])
print("As duas:", python & ingles)
print("Só Python:", python - ingles)
print("Total de alunos diferentes:", len(python | ingles))
