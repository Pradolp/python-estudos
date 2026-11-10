# Aula 07 - Exercícios
# Rode com: python aula07/exercicio.py

# -----------------------------------------------------------------------------
# Exercício 1: Ficha do jogador
# Leia o nome de um jogador e quantas partidas ele jogou. Depois leia quantos
# gols ele fez em cada partida. Guarde tudo num dicionário assim:
#   {"nome": "Rafa", "gols": [2, 0, 1], "total": 3}
# Mostre o dicionário e depois cada partida: "Partida 1: 2 gols"
# Escreva seu código aqui:
#%%
gols = []
jogador = {"nome": input("Digite seu nome:"), "gols": gols}
partidas = int(input("Quantidade de partidas disputadas? "))
for i in range(1, partidas + 1):
    gols.append(int(input(f"Quantidade de gols na Partida {i}")))
jogador["total"] = sum(gols)
print("PRINT DICIONARIO:")
print(jogador)
for i, valor in enumerate(gols, start=1):
    print(f"Partida {i}: {valor}")




# -----------------------------------------------------------------------------
# Exercício 2: Contador de letras
# Leia uma frase e mostre quantas vezes cada letra aparece (ignore espaços e
# não diferencie maiúsculas de minúsculas). Mostre em ordem alfabética.
# Dica: sorted(dicionario) devolve as chaves em ordem.
# Escreva seu código aqui:
#%%
frase = "Estou me cagando"
frase = frase.lower().replace(" ", "")
contagem_letras = {}
for letra in frase:
    contagem_letras[letra] = contagem_letras.get(letra, 0) + 1
#sorted sempre retorna uma lista então se eu usar direto no dict ele vai retornar somente as chaves 
for letra in sorted(contagem_letras):
    print(letra, contagem_letras[letra], end=" ")

# -----------------------------------------------------------------------------
# Exercício 3: Cadastro de pessoas
# Cadastre pessoas (nome e idade) até o usuário responder "N" para
# "Quer continuar? [S/N]". Guarde cada pessoa como um dicionário dentro de uma
# lista. No fim mostre:
#   - quantas pessoas foram cadastradas
#   - a média de idade
#   - os nomes das pessoas com idade acima da média
# Escreva seu código aqui:
#%%
pessoas = []
while True:
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade"))
    pessoas.append({"nome": nome, "idade": idade})
    continuar = input("Quer continuar? [S/N]").strip().upper()
    if continuar == "N":
        break
print(f"Quantidade pessoas cadastras {len(pessoas)}")
media = sum([dic["idade"] for dic in pessoas]) / len(pessoas)
idade_acima_media = [dic["nome"] for dic in pessoas if dic["idade"] > media]
print(f"Media de idade: {media:.1f}")
print("Pessoas acima da idade media: ", idade_acima_media)
 # %%


# -----------------------------------------------------------------------------
# Exercício 4: Estoque
# Dado o estoque abaixo, faça um programa que pede o nome de um produto e a
# quantidade a vender. Se o produto não existir ou não houver quantidade
# suficiente, avise. Se der certo, desconte do estoque e mostre o estoque final.
#%%
estoque = {"caneta": 10, "caderno": 5, "borracha": 0}
# Escreva seu código aqui:
produto = input("Produto: ").lower()
if produto not in estoque:
    print("Produto não existe")
else:
    quantidade = int(input("Quantidade: "))
    if quantidade > estoque[produto]:
        print("Não temos estoque")
    else:
        estoque[produto] -= quantidade
        print("Venda feita!")
print("Estoque final:", estoque)
        
# -----------------------------------------------------------------------------
# Exercício 5: Alunos em comum
# Usando conjuntos, descubra quem faz as duas matérias, quem faz só Python
# e quantos alunos diferentes existem no total.
#%%
python = ["Ana", "Bruno", "Carla", "Diego", "Ana"]
ingles = ["Carla", "Eva", "Bruno", "Fábio"]
# Escreva seu código aqui:

python = set(["Ana", "Bruno", "Carla", "Diego", "Ana"])
ingles = set(["Carla", "Eva", "Bruno", "Fábio"])
print("As duas:", python & ingles)
print("Só Python:", python - ingles)
print("Total de alunos diferentes:", len(python | ingles))