# Aula 01: variáveis, tipos, `print` e `input`

## 1. O que é uma variável

Uma variável é um **nome que guarda um valor**. Pense numa etiqueta colada numa caixa.

```python
nome = "Ana"
idade = 25
```

O sinal `=` **não** significa "igual" como na matemática. Ele significa
"guarde o valor da direita no nome da esquerda". Por isso isto é válido:

```python
pontos = 10
pontos = pontos + 5   # pega o valor atual (10), soma 5 e guarda de novo: 15
```

### Regras para nomes

- Podem ter letras, números e `_`, mas **não podem começar com número**.
- Não podem ter espaço. Acentos funcionam, mas é recomendado evitar (`preco`, não `preço`).
- Maiúsculas e minúsculas são diferentes: `idade` e `Idade` são variáveis distintas.
- Não use palavras reservadas do Python (`if`, `for`, `class`, `True`…).
- Convenção do Python: **snake_case**, com palavras minúsculas separadas por `_`:
  `nota_final`, `total_de_alunos`.

## 2. Tipos básicos

Todo valor tem um tipo. Os quatro primeiros que você precisa conhecer:

| Tipo    | Nome       | Exemplos                    |
|---------|------------|-----------------------------|
| `int`   | inteiro    | `10`, `-3`, `0`             |
| `float` | decimal    | `3.14`, `-0.5`, `2.0`       |
| `str`   | texto      | `"olá"`, `'Python'`, `"42"` |
| `bool`  | lógico     | `True`, `False`             |

Há também `None`, que significa "nenhum valor".

> Atenção: o decimal usa **ponto**, não vírgula: `1.75`, e não `1,75`.

A função `type()` mostra o tipo de um valor:

```python
type(10)      # <class 'int'>
type("10")    # <class 'str'>  — entre aspas é texto, mesmo sendo dígitos!
```

## 3. Mostrando coisas na tela: `print`

```python
print("Olá, mundo!")
print("Nome:", nome, "Idade:", idade)  # a vírgula separa itens e coloca espaço
```

A forma mais usada hoje é a **f-string**: coloque `f` antes das aspas e as variáveis
entre `{}`:

```python
print(f"{nome} tem {idade} anos")
print(f"Altura: {1.756:.2f}")   # :.2f = 2 casas decimais -> 1.76
```

## 4. Lendo o que o usuário digita: `input`

```python
nome = input("Qual é o seu nome? ")
```

`input` **sempre devolve texto (`str`)**, mesmo que a pessoa digite um número.
Para fazer contas é preciso converter:

```python
idade = int(input("Idade: "))       # texto -> inteiro
altura = float(input("Altura: "))   # texto -> decimal
```

### Conversões

| Função    | Converte para | Exemplo                 |
|-----------|---------------|-------------------------|
| `int()`   | inteiro       | `int("7")` vira `7`     |
| `float()` | decimal       | `float("1.5")` vira `1.5` |
| `str()`   | texto         | `str(42)` vira `"42"`   |
| `bool()`  | lógico        | `bool(0)` vira `False`  |

Se a conversão for impossível (`int("abc")`), o Python mostra um erro `ValueError`.
Na aula 09 você vai aprender a tratar isso.

## 5. Comentários

Tudo depois de `#` é ignorado pelo Python. Use para explicar o **porquê** do código.

```python
taxa = 0.1  # 10% de gorjeta, padrão em restaurantes
```

## Resumo

- `nome = valor` cria ou atualiza uma variável.
- Tipos básicos: `int`, `float`, `str`, `bool` (e `None`).
- `print(f"...{variavel}...")` mostra valores formatados.
- `input()` lê texto; converta com `int()` ou `float()` antes de fazer contas.

Agora rode `python aula01/exemplos.py` e depois faça o `exercicio.py`.
