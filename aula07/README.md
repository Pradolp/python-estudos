# Aula 07: dicionários, tuplas e conjuntos

## 1. Dicionários: valores com nome

Na lista você acessa os itens pela **posição**. No dicionário você acessa pela
**chave**, que é um nome que você escolhe.

```python
aluno = {
    "nome": "Ana",
    "idade": 21,
    "curso": "ADS",
}
aluno["nome"]    # 'Ana'
```

Cada item é um par `chave: valor`. As chaves costumam ser strings e **não se
repetem**. Os valores podem ser de qualquer tipo, inclusive listas e outros
dicionários.

> Dicionários são a estrutura mais importante para a sua trilha de IA. O JSON que
> as APIs devolvem vira dicionário em Python, e as mensagens de um chat com LLM
> são dicionários: `{"role": "user", "content": "Olá"}`.

## 2. Lendo valores com segurança

```python
aluno["email"]                  # KeyError: a chave não existe!
aluno.get("email")              # None (não dá erro)
aluno.get("email", "sem email") # 'sem email' (valor padrão)
"email" in aluno                # False (o "in" verifica as CHAVES)
```

## 3. Adicionando, alterando e removendo

```python
aluno["email"] = "ana@email.com"   # chave nova: adiciona
aluno["idade"] = 22                # chave existente: altera
del aluno["curso"]                 # remove
idade = aluno.pop("idade")         # remove e devolve o valor
aluno.update({"cidade": "Recife", "ativo": True})  # adiciona/altera vários
```

## 4. Percorrendo

```python
for chave in aluno:                  # percorre as chaves
    print(chave)

for chave, valor in aluno.items():   # chave e valor juntos (o mais usado)
    print(f"{chave}: {valor}")

aluno.keys()     # só as chaves
aluno.values()   # só os valores
```

## 5. Padrão "contador"

Contar quantas vezes cada coisa aparece:

```python
contagem = {}
for palavra in ["sol", "mar", "sol"]:
    contagem[palavra] = contagem.get(palavra, 0) + 1
# {'sol': 2, 'mar': 1}
```

## 6. Lista de dicionários

É o formato de "tabela" que você vai ver o tempo todo (resposta de API, linhas de
banco de dados, histórico de chat):

```python
alunos = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 6.5},
]
for a in alunos:
    print(a["nome"], a["nota"])
```

## 7. Tuplas: listas que não mudam

```python
ponto = (3, 4)
cores = ("vermelho", "verde", "azul")
ponto[0]          # 3
ponto[0] = 10     # TypeError: tupla é imutável
```

Use tupla para dados fixos que andam juntos. O uso mais comum é o
**desempacotamento**:

```python
x, y = ponto              # x = 3, y = 4
a, b = b, a               # troca valores (a direita é uma tupla)
```

## 8. Conjuntos (set): sem repetição e sem ordem

```python
numeros = {1, 2, 2, 3}       # {1, 2, 3}
vazio = set()                 # {} vazio é dicionário, não set!
numeros.add(4)
numeros.discard(1)
set([3, 1, 3, 2])             # remove duplicados de uma lista

a = {1, 2, 3}
b = {2, 3, 4}
a | b    # união:      {1, 2, 3, 4}
a & b    # interseção: {2, 3}
a - b    # diferença:  {1}
```

`x in conjunto` é muito rápido, mesmo com milhões de itens.

## Quando usar cada um

| Estrutura | Símbolo | Ordem | Muda? | Repete? | Use para…                      |
|-----------|---------|-------|-------|---------|--------------------------------|
| lista     | `[]`    | sim   | sim   | sim     | sequência de itens             |
| tupla     | `()`    | sim   | não   | sim     | dados fixos que andam juntos   |
| dicionário| `{k: v}`| sim*  | sim   | chaves não | dados com nome              |
| conjunto  | `{}`    | não   | sim   | não     | itens únicos, testes de "está em" |

\* Desde o Python 3.7, o dicionário mantém a ordem em que as chaves foram inseridas.
