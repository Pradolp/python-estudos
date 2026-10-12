# Aula 12: orientação a objetos, classes e métodos

## 1. A ideia

Até agora os **dados** (variáveis, dicionários) ficaram separados das **ações**
(funções). Na orientação a objetos, você junta os dois:

- uma **classe** é o molde, por exemplo "Conta bancária";
- um **objeto** (ou instância) é algo criado a partir do molde, como "a conta da Ana";
- **atributos** são os dados do objeto (`titular`, `saldo`);
- **métodos** são as funções do objeto (`depositar()`, `sacar()`).

Você já usa objetos o tempo todo: `"texto".upper()` chama o método `upper` de um
objeto `str`, e `lista.append(x)` chama um método de um objeto `list`.

## 2. Criando uma classe

```python
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome        # atributo
        self.idade = idade

    def latir(self):            # método
        return f"{self.nome} diz: Au au!"


rex = Cachorro("Rex", 3)       # cria um objeto (chama o __init__)
print(rex.nome)                # Rex
print(rex.latir())             # Rex diz: Au au!
```

- Nome de classe usa **PascalCase**: `ContaBancaria`, `Cachorro`.
- `__init__` é o **construtor**: roda automaticamente ao criar o objeto e prepara
  os atributos.
- `self` é **o próprio objeto**. Todo método recebe `self` como primeiro parâmetro,
  mas você não passa esse valor na chamada; o Python passa sozinho.
  `rex.latir()` vira, por baixo, `Cachorro.latir(rex)`.

## 3. Cada objeto tem os seus dados

```python
rex = Cachorro("Rex", 3)
bob = Cachorro("Bob", 5)
bob.idade += 1
print(rex.idade, bob.idade)   # 3 6
```

## 4. Métodos que mudam o estado

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("depósito deve ser positivo")
        self.saldo += valor
```

Isso junta tudo o que você aprendeu: parâmetros padrão (aula 08), `raise` (aula 09)
e `if` (aula 03).

## 5. `__str__`: como o objeto aparece no `print`

```python
class Cachorro:
    ...
    def __str__(self):
        return f"Cachorro {self.nome}, {self.idade} anos"

print(rex)   # Cachorro Rex, 3 anos  (sem __str__: <__main__.Cachorro object at 0x...>)
```

Métodos com `__dois_sublinhados__` são chamados de **métodos especiais**. O Python
os chama em situações específicas (`__init__` ao criar, `__str__` no `print`,
`__len__` no `len()`...).

## 6. Atributos de classe

Valem para **todos** os objetos da classe:

```python
class Cachorro:
    especie = "Canis familiaris"   # atributo de classe

    def __init__(self, nome):
        self.nome = nome           # atributo de instância
```

## 7. Encapsulamento por convenção

Em Python, um atributo que começa com `_` sinaliza: "isto é interno, não mexa
diretamente, use os métodos".

```python
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0.0          # interno: altere só via depositar/sacar

    @property
    def saldo(self):               # permite LER conta.saldo, mas não atribuir
        return self._saldo
```

`@property` faz um método ser lido como se fosse atributo (`conta.saldo`, sem
parênteses).

## 8. Herança: uma classe baseada em outra

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "..."


class Gato(Animal):              # Gato herda tudo de Animal
    def falar(self):             # e substitui (sobrescreve) o que quiser
        return f"{self.nome}: Miau"


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)   # reaproveita o __init__ do Animal
        self.raca = raca

    def falar(self):
        return f"{self.nome}: Au au"
```

Com herança, objetos diferentes respondem ao mesmo método cada um do seu jeito:

```python
for bicho in [Gato("Mimi"), Cachorro("Rex", "vira-lata")]:
    print(bicho.falar())
```

## 9. Onde isso aparece no roadmap

- `class Pergunta(BaseModel):` no FastAPI (fase 2 e fase 8) é uma classe que herda
  de `BaseModel` do Pydantic.
- `modelo = init_chat_model(...)` devolve um objeto, e `modelo.invoke(...)` é um método dele.
- `resposta.content` é um atributo do objeto de resposta.

Você não vai precisar criar hierarquias complicadas. O essencial é **ler e usar**
classes com tranquilidade e saber criar as suas quando os dados e as ações andam juntos.

## Resumo

- `class Nome:` define o molde; `Nome(...)` cria um objeto.
- `__init__(self, ...)` prepara os atributos; `self` é o próprio objeto.
- Métodos são funções dentro da classe e sempre recebem `self`.
- `__str__` define o texto do `print`.
- `class Filha(Mae):` herda; `super().__init__(...)` reaproveita o construtor.
