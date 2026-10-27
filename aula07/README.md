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
len(aluno)       # quantos pares chave: valor existem
```

> Não existe `enumerate` para dicionário porque a **chave já faz o papel do
> índice**. O `.items()` é o "enumerate" do dicionário.

## 5. Resumo dos métodos de dicionário

Estes são os que você vai usar de verdade:

| Método                  | O que faz                                              |
|-------------------------|--------------------------------------------------------|
| `d.get(k, padrao)`      | lê `k`; se não existir, devolve `padrao` (ou `None`)   |
| `d.keys()`              | as chaves                                              |
| `d.values()`            | os valores                                             |
| `d.items()`             | os pares `(chave, valor)`                              |
| `d.update(outro)`       | adiciona/altera vários pares de uma vez                |
| `d.pop(k)`              | remove `k` e devolve o valor dele                      |
| `d.setdefault(k, v)`    | se `k` não existe, cria com `v`; devolve o valor de `k`|
| `d.copy()`              | cria uma cópia (veja o aviso abaixo)                   |
| `d.clear()`             | esvazia o dicionário                                   |

**Aviso sobre cópia:** `copia = aluno` **não copia**, só cria outro nome para o
mesmo dicionário. Alterar um altera o outro. Para copiar de verdade, use
`aluno.copy()`.

```python
original = {"nome": "Ana"}
outro_nome = original
outro_nome["nome"] = "Bia"
print(original)   # {'nome': 'Bia'}  ← mudou também!
```

Para ver **todos** os métodos, use `help(dict)` ou `dir(dict)` no terminal. Não
precisa decorar: você consulta quando precisar.

## 6. Padrão "contador"

Contar quantas vezes cada coisa aparece:

```python
contagem = {}
for palavra in ["sol", "mar", "sol"]:
    contagem[palavra] = contagem.get(palavra, 0) + 1
# {'sol': 2, 'mar': 1}
```

O `get(palavra, 0)` devolve 0 na primeira vez que a palavra aparece, então a conta
vira `0 + 1`. Nas próximas vezes ele pega o valor que já estava lá e soma 1.

Para achar a chave com o **maior valor**, use `max` com `key`:

```python
mais_comum = max(contagem, key=contagem.get)   # 'sol'
```

Sem o `key`, o `max` compararia as chaves pela ordem alfabética. Com
`key=contagem.get`, ele compara pelos valores (as contagens).

## 7. Lista de dicionários

É o formato de "tabela" que você vai ver o tempo todo (resposta de API, linhas de
banco de dados, histórico de chat):

```python
alunos = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 6.5},
]
for a in alunos:
    print(a["nome"], a["nota"])

media = sum(a["nota"] for a in alunos) / len(alunos)   # média das notas
```

Como é uma **lista**, você adiciona um item novo com `append`:

```python
alunos.append({"nome": "Carla", "nota": 7.8})
```

## 8. Dicionário com lista dentro

O valor de uma chave pode ser uma lista. Aí você usa os **métodos de lista** nesse
valor:

```python
turma = {"professor": "Marcos", "alunos": ["Ana", "Bruno"]}

turma["alunos"].append("Diego")   # ["Ana", "Bruno", "Diego"]
len(turma["alunos"])              # 3
```

Leia em duas etapas: `turma["alunos"]` devolve a lista, e o `.append(...)` age
**nessa lista**. O `append` não é método de dicionário, é de lista.

Cuidado para não trocar por uma atribuição:

```python
turma["alunos"] = "Diego"   # substitui a lista inteira pela string "Diego"!
```

## 9. Tuplas: listas que não mudam

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

## 10. Conjuntos (set): sem repetição e sem ordem

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
