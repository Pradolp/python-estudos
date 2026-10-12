# Aula 08: funções

## 1. Por que funções

Uma função é um **bloco de código com nome** que você escreve uma vez e usa quantas
vezes quiser. Você já usou várias: `print()`, `len()`, `input()`. Agora vai criar as
suas.

Vantagens:
- evita repetir código;
- divide um problema grande em partes pequenas;
- dá nome ao que o código faz (`calcular_media(notas)` é mais fácil de ler que 4 linhas soltas).

## 2. Definindo e chamando

```python
def saudar():
    print("Olá!")

saudar()   # chamada: só aqui o código de dentro roda
```

## 3. Parâmetros e `return`

```python
def somar(a, b):     # a e b são PARÂMETROS
    return a + b     # devolve o resultado para quem chamou

resultado = somar(3, 4)   # 3 e 4 são ARGUMENTOS
print(resultado)          # 7
```

**`print` x `return`**, a confusão mais comum:

- `print` só **mostra** o valor na tela.
- `return` **devolve** o valor para o programa usar (guardar, somar, comparar...).
- Uma função sem `return` devolve `None`.
- O `return` também **encerra** a função na hora.

```python
def dobro_errado(n):
    print(n * 2)       # mostra, mas não devolve

x = dobro_errado(5)    # mostra 10
print(x + 1)           # TypeError: None + 1
```

## 4. Valores padrão e argumentos nomeados

```python
def cumprimentar(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

cumprimentar("Ana")                       # 'Olá, Ana!'
cumprimentar("Ana", "Bom dia")            # 'Bom dia, Ana!'
cumprimentar(saudacao="Oi", nome="Bruno") # nomeados: a ordem não importa
```

Os parâmetros com valor padrão vêm sempre **depois** dos que não têm.

Você já viu argumentos nomeados antes: `print("a", end="")`, `sorted(x, reverse=True)`.
No roadmap eles aparecem o tempo todo, como em `init_chat_model("...", temperature=0.7)`.

## 5. Devolvendo vários valores

```python
def estatisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

menor, maior, media = estatisticas([4, 8, 6])   # devolve uma tupla
```

## 6. Escopo: onde a variável existe

Variáveis criadas **dentro** de uma função só existem lá dentro (escopo local).

```python
def f():
    x = 10
f()
print(x)   # NameError: x não existe aqui fora
```

A função consegue **ler** variáveis de fora, mas o ideal é receber tudo por
parâmetro e devolver com `return`. Assim a função fica previsível e fácil de testar.

## 7. Docstring e dicas de tipo

```python
def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o Índice de Massa Corporal (peso em kg, altura em metros)."""
    return peso / altura ** 2
```

- **Docstring** (texto entre `"""` na primeira linha) explica o que a função faz.
  Aparece quando você passa o mouse sobre a função no VS Code. Na fase 7 do roadmap,
  é a docstring que o modelo de IA lê para decidir quando usar a sua ferramenta `@tool`.
- **Type hints** (`: float`, `-> float`) dizem os tipos esperados. O Python não
  obriga, mas o VS Code usa para avisar erros, e o FastAPI/Pydantic (fase 2) usa para
  validar dados.

## 8. `*args` (bônus)

Para aceitar qualquer quantidade de argumentos:

```python
def somar_tudo(*numeros):      # numeros vira uma tupla
    return sum(numeros)

somar_tudo(1, 2, 3, 4)   # 10
```

## 9. Funções chamando funções

```python
def eh_par(n):
    return n % 2 == 0

def filtrar_pares(numeros):
    return [n for n in numeros if eh_par(n)]
```

Boa prática: **cada função faz uma coisa só**. Se o nome precisa de "e"
(`ler_e_calcular_e_mostrar`), provavelmente dá para dividir.

## Resumo

- `def nome(parametros):` cria; `nome(argumentos)` chama.
- `return` devolve um valor e encerra a função; `print` só mostra.
- Parâmetros podem ter valor padrão; argumentos podem ser passados pelo nome.
- Variáveis de dentro da função não existem fora dela.
- Escreva docstrings: elas documentam o código e, na trilha de IA, instruem o modelo.
