# Aula 07 - Exemplos: dicionários, tuplas e conjuntos
# Rode com: python aula07/exemplos.py

print("=== Criando um dicionário ===")
aluno = {"nome": "Ana", "idade": 21, "curso": "ADS"}
print(aluno)
print("Nome:", aluno["nome"])

print("\n=== get e in ===")
print("get('email'):", aluno.get("email"))
print("get('email', 'sem email'):", aluno.get("email", "sem email"))
print("'curso' in aluno?", "curso" in aluno)

print("\n=== Alterando ===")
aluno["email"] = "ana@email.com"
aluno["idade"] = 22
del aluno["curso"]
aluno.update({"cidade": "Recife"})
print(aluno)

print("\n=== Percorrendo ===")
for chave, valor in aluno.items():
    print(f"  {chave:>7}: {valor}")  # :>7 alinha à direita em 7 espaços
print("Chaves:", list(aluno.keys()))
print("Valores:", list(aluno.values()))

print("\n=== Contador de palavras ===")
texto = "o sol nasce o sol se põe e o mar fica"
contagem = {}
for palavra in texto.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)
mais_comum = max(contagem, key=contagem.get)  # chave com o maior valor
print(f"Mais comum: '{mais_comum}' ({contagem[mais_comum]} vezes)")

print("\n=== Lista de dicionários ===")
alunos = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 6.5},
    {"nome": "Carla", "nota": 7.8},
]
for a in alunos:
    situacao = "aprovado" if a["nota"] >= 7 else "reprovado"
    print(f"{a['nome']:<6} {a['nota']:>4}  {situacao}")
media = sum(a["nota"] for a in alunos) / len(alunos)
print(f"Média da turma: {media:.2f}")

print("\n=== Dicionário com lista dentro ===")
turma = {"professor": "Marcos", "alunos": ["Ana", "Bruno", "Carla"]}
turma["alunos"].append("Diego")
print(f"{turma['professor']} tem {len(turma['alunos'])} alunos: {turma['alunos']}")

print("\n=== Isto é o formato de um chat com LLM (fase 4 do roadmap) ===")
historico = [
    {"role": "system", "content": "Você é um assistente simpático."},
    {"role": "user", "content": "Olá!"},
]
historico.append({"role": "assistant", "content": "Oi! Como posso ajudar?"})
for mensagem in historico:
    print(f"[{mensagem['role']}] {mensagem['content']}")

print("\n=== Tuplas ===")
ponto = (3, 4)
x, y = ponto
print(f"x = {x}, y = {y}")
a, b = 1, 2
a, b = b, a
print(f"Depois da troca: a = {a}, b = {b}")
for nome, nota in [("Ana", 9.0), ("Bruno", 6.5)]:  # desempacotando no for
    print(nome, nota)

print("\n=== Conjuntos ===")
numeros = {1, 2, 2, 3, 3, 3}
print("Sem repetidos:", numeros)
python = {"Ana", "Bruno", "Carla"}
sql = {"Bruno", "Carla", "Diego"}
print("Sabem os dois:", python & sql)
print("Sabem pelo menos um:", python | sql)
print("Só Python:", python - sql)
