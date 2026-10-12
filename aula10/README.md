# Aula 10: módulos e pacotes

## 1. O que é um módulo

Um **módulo** é simplesmente um arquivo `.py`. Quando um programa cresce, você
separa o código em vários arquivos e **importa** o que precisa de cada um.

O Python já vem com centenas de módulos prontos, a **biblioteca padrão**
("baterias incluídas").

## 2. Formas de importar

```python
import math                    # importa o módulo inteiro
math.sqrt(16)                  # usa com o prefixo: 4.0

from math import sqrt, pi      # importa só alguns nomes
sqrt(16)                       # usa sem prefixo

import datetime as dt          # apelido
dt.date.today()

from math import *             # importa tudo: EVITE, você perde a noção de onde veio cada nome
```

Coloque os `import` **no topo do arquivo**.

## 3. Módulos da biblioteca padrão que valem conhecer já

| Módulo     | Para que serve                         | Exemplo                                   |
|------------|----------------------------------------|-------------------------------------------|
| `math`     | matemática                             | `math.sqrt(2)`, `math.pi`, `math.ceil(2.1)` |
| `random`   | sorteios                               | `random.randint(1, 10)`, `random.choice(lista)` |
| `datetime` | datas e horas                          | `datetime.date.today()`                   |
| `time`     | pausas e tempo                         | `time.sleep(1)`                           |
| `pathlib`  | caminhos e arquivos                    | `Path("dados.txt").exists()`              |
| `json`     | ler e escrever JSON                    | `json.dumps(dicionario)`                  |
| `os`       | sistema operacional, variáveis de ambiente | `os.getenv("GOOGLE_API_KEY")`         |
| `sys`      | informações do Python                  | `sys.version`                             |

Para descobrir o que um módulo tem: `help(math)` ou `dir(math)` no terminal
interativo do Python (digite `python` no terminal e depois `exit()` para sair).

## 4. Criando seu próprio módulo

Crie um arquivo `calculos.py`:

```python
# calculos.py
def dobro(n):
    return n * 2
```

E em outro arquivo **na mesma pasta**:

```python
# programa.py
import calculos
print(calculos.dobro(5))
```

> Não dê ao seu arquivo o nome de um módulo existente (`random.py`, `math.py`,
> `json.py`). O Python vai importar o seu arquivo no lugar do original e nada vai
> funcionar.

## 5. `if __name__ == "__main__":`

Quando você importa um módulo, **todo o código dele roda**. Para ter código que só
roda quando o arquivo é executado diretamente (e não quando é importado), use:

```python
def dobro(n):
    return n * 2

if __name__ == "__main__":
    # só roda com: python calculos.py
    print("Testando:", dobro(5))
```

`__name__` vale `"__main__"` no arquivo que você mandou rodar e vale o nome do módulo
(`"calculos"`) quando ele é importado. Você vai ver esse padrão no `agente.py` da
fase 7 do roadmap.

## 6. Pacotes: pastas de módulos

Um **pacote** é uma pasta com módulos dentro e um arquivo `__init__.py` (pode
ficar vazio). Nesta aula há um exemplo:

```
aula10/
├── exemplos.py
└── ferramentas/          <- pacote
    ├── __init__.py
    ├── textos.py         <- módulo
    └── numeros.py        <- módulo
```

```python
from ferramentas import textos
from ferramentas.numeros import eh_par
from ferramentas.textos import remover_acentos as sem_acento
```

O `__init__.py` pode reexportar nomes para facilitar o import:

```python
# ferramentas/__init__.py
from .numeros import eh_par    # o ponto significa "deste pacote"
```

Permite fazer `from ferramentas import eh_par`.

## 7. E os pacotes de terceiros?

Módulos que **não** vêm com o Python (como `requests`, `fastapi`, `langchain`) são
instalados com o `pip`. Isso é o assunto da próxima aula.

## Resumo

- Módulo = arquivo `.py`; pacote = pasta com `__init__.py` e módulos.
- `import modulo`, `from modulo import nome`, `import modulo as apelido`.
- A biblioteca padrão já resolve muita coisa: `math`, `random`, `datetime`, `json`, `os`.
- `if __name__ == "__main__":` separa o código de teste do código reutilizável.
- Nunca dê ao seu arquivo o nome de um módulo que já existe.
