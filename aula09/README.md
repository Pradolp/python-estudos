# Aula 09: tratamento de erros (`try` / `except`)

## 1. Erros acontecem

Quando algo dá errado durante a execução, o Python **lança uma exceção** e o
programa para, mostrando uma mensagem chamada *traceback*:

```
Traceback (most recent call last):
  File "programa.py", line 1, in <module>
    idade = int(input("Idade: "))
ValueError: invalid literal for int() with base 10: 'vinte'
```

Leia o traceback **de baixo para cima**: a última linha diz o tipo do erro e o
motivo; as linhas acima dizem onde ele aconteceu.

## 2. Exceções mais comuns

| Exceção             | Quando acontece                               | Exemplo               |
|---------------------|-----------------------------------------------|-----------------------|
| `ValueError`        | valor com formato errado                      | `int("abc")`          |
| `TypeError`         | operação com tipo errado                      | `"a" + 1`             |
| `ZeroDivisionError` | divisão por zero                              | `10 / 0`              |
| `IndexError`        | posição que não existe na lista               | `[1, 2][5]`           |
| `KeyError`          | chave que não existe no dicionário            | `{"a": 1}["b"]`       |
| `NameError`         | variável que não foi criada                   | `print(xyz)`          |
| `FileNotFoundError` | arquivo que não existe                        | `open("nada.txt")`    |

> `SyntaxError` e `IndentationError` são diferentes: o Python nem começa a rodar o
> programa. Esses erros você corrige no código, não com `try`.

## 3. `try` / `except`

```python
try:
    idade = int(input("Idade: "))
    print(f"Ano que vem você terá {idade + 1}")
except ValueError:
    print("Digite apenas números!")
```

O Python tenta executar o bloco `try`. Se acontecer um `ValueError`, ele pula
direto para o `except` em vez de parar o programa.

## 4. Vários `except`

```python
try:
    a = int(input("A: "))
    b = int(input("B: "))
    print(a / b)
except ValueError:
    print("Digite números inteiros.")
except ZeroDivisionError:
    print("Não dá para dividir por zero.")
```

Você pode pegar a mensagem do erro com `as`:

```python
except ValueError as erro:
    print("Erro:", erro)
```

## 5. `else` e `finally`

```python
try:
    arquivo = open("dados.txt")
except FileNotFoundError:
    print("Arquivo não encontrado.")
else:
    print("Abriu!")          # só roda se NÃO deu erro
    arquivo.close()
finally:
    print("Fim da tentativa")  # roda SEMPRE, com ou sem erro
```

## 6. Não engula erros

```python
try:
    ...
except:              # ruim: pega TUDO, até Ctrl+C e erros de digitação no código
    pass
```

- Sempre diga **qual** exceção espera (`except ValueError:`).
- Coloque no `try` só as linhas que podem falhar.
- Se precisar de um "pega tudo", use `except Exception as erro:` e **mostre** o erro.

## 7. Lançando seus próprios erros: `raise`

Suas funções também podem avisar que receberam algo inválido:

```python
def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo.")
    if valor > saldo:
        raise ValueError("Saldo insuficiente.")
    return saldo - valor
```

Quem chama a função decide o que fazer com o erro (`try/except`). Essa divisão é
importante: a função **detecta** o problema e quem a chama decide como **lidar** com ele.

## 8. Padrão: pedir até a entrada ser válida

Une `while True` (aula 04), funções (aula 08) e `try`:

```python
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido, tente novamente.")
```

Esse padrão vai aparecer no seu mini projeto (aula 14).

## Resumo

- Leia o traceback de baixo para cima.
- `try:` código arriscado; `except TipoDoErro:` o que fazer se falhar.
- `else` roda se deu certo e `finally` roda sempre.
- Use `raise ValueError("mensagem")` para recusar dados inválidos nas suas funções.
- Nunca use `except:` vazio com `pass`.
