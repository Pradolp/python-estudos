# Aula 05: repetição com `for` e `range`

## 1. `for` percorre uma sequência

O `while` repete enquanto uma condição for verdadeira. O `for` repete **uma vez para
cada item** de uma sequência, e você não precisa controlar um contador.

```python
for letra in "Python":
    print(letra)
```

A cada volta, a variável `letra` recebe o próximo item: `P`, depois `y`, depois `t`...

## 2. `range`: gerar sequências de números

| Chamada            | Gera                  |
|--------------------|-----------------------|
| `range(5)`         | 0, 1, 2, 3, 4         |
| `range(1, 6)`      | 1, 2, 3, 4, 5         |
| `range(0, 11, 2)`  | 0, 2, 4, 6, 8, 10     |
| `range(10, 0, -1)` | 10, 9, 8, ..., 1      |

Formato: `range(início, fim, passo)`. O **fim nunca entra** (igual ao fatiamento de
strings). Se você passa um número só, ele é o fim e o início é 0.

```python
for i in range(1, 6):
    print(f"Volta {i}")
```

## 3. `for` ou `while`?

| Use `for` quando…                          | Use `while` quando…                         |
|--------------------------------------------|---------------------------------------------|
| sabe quantas vezes vai repetir             | não sabe quantas vezes vai repetir          |
| vai percorrer os itens de uma sequência    | depende de algo que o usuário digita        |
| exemplo: tabuada de 1 a 10                 | exemplo: "leia até digitar 0"               |

## 4. `enumerate`: item e posição juntos

```python
for posicao, letra in enumerate("abc"):
    print(posicao, letra)    # 0 a / 1 b / 2 c

for numero, letra in enumerate("abc", start=1):
    print(numero, letra)     # 1 a / 2 b / 3 c
```

## 5. `break`, `continue` e `else`

`break` e `continue` funcionam igual ao `while`. Existe ainda um `else` no laço que
roda **só se o laço terminou sem `break`**. Ele é útil para buscas:

```python
for n in range(2, 10):
    if 37 % n == 0:
        print("Achei um divisor:", n)
        break
else:
    print("Nenhum divisor entre 2 e 9")
```

## 6. Laços aninhados

Um `for` dentro de outro: o de dentro roda inteiro a cada volta do de fora.

```python
for linha in range(1, 4):
    for coluna in range(1, 4):
        print(f"({linha},{coluna})", end=" ")
    print()   # quebra de linha ao fim de cada linha
```

## 7. A variável `_`

Quando você só quer repetir e não usa a variável, a convenção é chamá-la de `_`:

```python
for _ in range(3):
    print("Olá!")
```

## Resumo

- `for item in sequencia:` repete uma vez para cada item.
- `range(início, fim, passo)` gera números; o fim não entra.
- `enumerate` devolve posição e item juntos.
- Use `for` quando a quantidade de repetições é conhecida e `while` quando não é.
