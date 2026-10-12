# Aula 02: operadores e textos (strings)

## 1. Operadores aritméticos

| Operador | Significado        | Exemplo   | Resultado |
|----------|--------------------|-----------|-----------|
| `+`      | soma               | `7 + 2`   | `9`       |
| `-`      | subtração          | `7 - 2`   | `5`       |
| `*`      | multiplicação      | `7 * 2`   | `14`      |
| `/`      | divisão            | `7 / 2`   | `3.5`     |
| `//`     | divisão inteira    | `7 // 2`  | `3`       |
| `%`      | resto da divisão   | `7 % 2`   | `1`       |
| `**`     | potência           | `7 ** 2`  | `49`      |

- `/` **sempre** devolve `float`, mesmo em `4 / 2` (resultado `2.0`).
- `%` (módulo) é muito útil: `n % 2 == 0` diz se `n` é par.
- A ordem é a da matemática: `**` primeiro, depois `* / // %`, depois `+ -`.
  Use parênteses quando estiver em dúvida: `(2 + 3) * 4`.

Atalhos de atribuição: `x += 1` é o mesmo que `x = x + 1`. Também existem
`-=`, `*=`, `/=`.

## 2. Operadores de comparação

Comparações sempre devolvem `True` ou `False`.

| Operador | Significado     |
|----------|-----------------|
| `==`     | igual           |
| `!=`     | diferente       |
| `>`  `<` | maior, menor    |
| `>=` `<=`| maior ou igual, menor ou igual |

> Não confunda `=` (guardar valor) com `==` (comparar).

## 3. Operadores lógicos

Combinam condições:

| Operador | Resultado é `True` quando…        |
|----------|-----------------------------------|
| `and`    | as **duas** condições são verdade |
| `or`     | **pelo menos uma** é verdade      |
| `not`    | inverte: `not True` é `False`     |

```python
idade = 20
tem_ingresso = True
pode_entrar = idade >= 18 and tem_ingresso   # True
```

## 4. Strings (textos)

Texto pode usar aspas simples ou duplas: `'oi'` ou `"oi"`.
Para várias linhas, use três aspas: `"""linha 1\nlinha 2"""`.

### Índices e fatiamento

Cada caractere tem uma posição, **começando do zero**:

```
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

```python
s = "Python"
s[0]     # 'P'
s[-1]    # 'n'  (índice negativo conta do fim)
s[0:3]   # 'Pyt' (do 0 até o 3, SEM incluir o 3)
s[2:]    # 'thon'
s[::-1]  # 'nohtyP' (invertido)
len(s)   # 6
```

Strings são **imutáveis**: `s[0] = "J"` dá erro. Você cria uma string nova.

### Métodos mais usados

| Método                | O que faz                                |
|-----------------------|------------------------------------------|
| `s.upper()`           | tudo maiúsculo                           |
| `s.lower()`           | tudo minúsculo                           |
| `s.title()`           | Primeira Letra De Cada Palavra           |
| `s.strip()`           | tira espaços do começo e do fim          |
| `s.replace("a", "b")` | troca trechos                            |
| `s.count("a")`        | quantas vezes aparece                    |
| `s.find("a")`         | posição da primeira ocorrência (-1 se não acha) |
| `s.split()`           | quebra em lista de palavras              |
| `s.startswith("x")`   | começa com…? (`True`/`False`)            |
| `"x" in s`            | contém…? (`True`/`False`)                |

Métodos não mudam a string original; eles devolvem uma nova:

```python
nome = "  ana  "
nome.strip()          # devolve "ana", mas nome continua "  ana  "
nome = nome.strip()   # agora sim nome vale "ana"
```

Você também pode repetir e juntar: `"ab" * 3` vira `"ababab"`, `"a" + "b"` vira `"ab"`.

## Resumo

- `//` dá a divisão inteira e `%` dá o resto; os dois aparecem em muitos exercícios.
- Comparações devolvem `bool`; `and`, `or` e `not` combinam essas comparações.
- Índices começam em 0, e o fatiamento `[início:fim]` não inclui o `fim`.
- Métodos como `.upper()` e `.strip()` devolvem uma string nova.
