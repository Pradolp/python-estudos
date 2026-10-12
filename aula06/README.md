# Aula 06: listas

## 1. O que é uma lista

Uma lista guarda **vários valores numa única variável**, em ordem.

```python
frutas = ["maçã", "banana", "uva"]
notas = [7.5, 8.0, 9.2]
misturada = [1, "dois", 3.0, True]   # pode misturar tipos (mas evite)
vazia = []
```

## 2. Acessando itens

Igual às strings: índice começa em 0 e índices negativos contam do fim.

```python
frutas[0]      # 'maçã'
frutas[-1]     # 'uva'
frutas[0:2]    # ['maçã', 'banana']
len(frutas)    # 3
"uva" in frutas  # True
```

Diferente das strings, **listas podem ser alteradas**:

```python
frutas[1] = "manga"   # ['maçã', 'manga', 'uva']
```

## 3. Adicionando e removendo

| Método / comando        | O que faz                                        |
|-------------------------|--------------------------------------------------|
| `lista.append(x)`       | adiciona `x` no fim                              |
| `lista.insert(i, x)`    | adiciona `x` na posição `i`                      |
| `lista.extend(outra)`   | adiciona todos os itens de outra lista           |
| `lista.remove(x)`       | remove a primeira ocorrência de `x`              |
| `lista.pop()`           | remove e **devolve** o último item               |
| `lista.pop(i)`          | remove e devolve o item da posição `i`           |
| `del lista[i]`          | apaga o item da posição `i`                      |
| `lista.clear()`         | esvazia a lista                                  |

## 4. Ordenando e buscando

| Método / função          | O que faz                                          |
|--------------------------|----------------------------------------------------|
| `lista.sort()`           | ordena **a própria lista** (não devolve nada)      |
| `lista.sort(reverse=True)` | ordena do maior para o menor                     |
| `sorted(lista)`          | devolve uma **nova** lista ordenada                |
| `lista.reverse()`        | inverte a ordem                                    |
| `lista.index(x)`         | posição da primeira ocorrência de `x`              |
| `lista.count(x)`         | quantas vezes `x` aparece                          |
| `sum`, `min`, `max`      | soma, menor e maior valor                          |

> Armadilha clássica: `lista = lista.sort()` deixa `lista` valendo `None`,
> porque `.sort()` não devolve nada. Use `lista.sort()` sozinho ou `nova = sorted(lista)`.

## 5. Percorrendo

```python
for fruta in frutas:
    print(fruta)

for i, fruta in enumerate(frutas):
    print(i, fruta)
```

Montando uma lista a partir de entradas:

```python
numeros = []
for _ in range(3):
    numeros.append(int(input("Número: ")))
```

## 6. Cópia x referência

```python
a = [1, 2, 3]
b = a          # b NÃO é uma cópia: é outro nome para a MESMA lista
b.append(4)
print(a)       # [1, 2, 3, 4]  — a também mudou!

c = a.copy()   # agora sim, uma cópia independente (ou a[:])
```

## 7. List comprehension

Um jeito curto de criar uma lista a partir de outra:

```python
quadrados = [n * n for n in range(1, 6)]          # [1, 4, 9, 16, 25]
pares = [n for n in range(10) if n % 2 == 0]      # [0, 2, 4, 6, 8]
nomes_maiusculos = [nome.upper() for nome in nomes]
```

Ela equivale a um `for` com `append`. Use quando ficar fácil de ler.

## 8. Listas dentro de listas

```python
matriz = [[1, 2, 3],
          [4, 5, 6]]
matriz[1][2]   # 6  (linha 1, coluna 2)
```

## 9. Juntando e separando com strings

```python
"a,b,c".split(",")           # ['a', 'b', 'c']
", ".join(["a", "b", "c"])   # 'a, b, c'
```

## Resumo

- Listas guardam vários valores em ordem e **podem ser alteradas**.
- `append` adiciona no fim, `remove`/`pop` tiram itens, `sort`/`sorted` ordenam.
- `b = a` não copia; use `a.copy()`.
- List comprehension: `[expressão for item in sequencia if condição]`.
