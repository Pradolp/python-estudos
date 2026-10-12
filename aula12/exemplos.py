# Aula 12 - Exemplos: classes e métodos
# Rode com: python aula12/exemplos.py


class Cachorro:
    especie = "Canis familiaris"  # atributo de classe: igual para todos

    def __init__(self, nome: str, idade: int):
        self.nome = nome  # atributos de instância: cada objeto tem os seus
        self.idade = idade
        self.truques = []

    def latir(self) -> str:
        return f"{self.nome} diz: Au au!"

    def aprender(self, truque: str) -> None:
        self.truques.append(truque)

    def fazer_aniversario(self) -> None:
        self.idade += 1

    def __str__(self) -> str:
        return f"{self.nome} ({self.idade} anos) sabe: {', '.join(self.truques) or 'nada ainda'}"


print("=== Criando objetos ===")
rex = Cachorro("Rex", 3)
bob = Cachorro("Bob", 5)
print(rex.latir())
print(bob.latir())
print("Espécie (atributo de classe):", rex.especie, "|", bob.especie)

print("\n=== Cada objeto tem seu estado ===")
rex.aprender("sentar")
rex.aprender("rolar")
bob.fazer_aniversario()
print(rex)  # chama __str__
print(bob)
print("Tipo do objeto:", type(rex).__name__)


class ContaBancaria:
    """Conta com saldo protegido: só muda via depositar e sacar."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self._saldo = saldo_inicial  # _ = interno, use os métodos
        self._historico = []

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("o depósito deve ser positivo")
        self._saldo += valor
        self._historico.append(f"+ {valor:8.2f}")

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("o saque deve ser positivo")
        if valor > self._saldo:
            raise ValueError(f"saldo insuficiente (saldo atual: {self._saldo:.2f})")
        self._saldo -= valor
        self._historico.append(f"- {valor:8.2f}")

    def extrato(self) -> str:
        linhas = [f"Extrato de {self.titular}"] + self._historico
        linhas.append(f"Saldo: {self._saldo:.2f}")
        return "\n".join(linhas)


print("\n=== Conta bancária ===")
conta = ContaBancaria("Ana", 100)
conta.depositar(50)
conta.sacar(30)
for operacao, valor in [("sacar", 500), ("depositar", -10)]:
    try:
        getattr(conta, operacao)(valor)  # chama conta.sacar(500), depois conta.depositar(-10)
    except ValueError as erro:
        print(f"{operacao}({valor}) recusado: {erro}")
print(conta.extrato())
print("Saldo via property:", conta.saldo)


print("\n=== Herança ===")


class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def falar(self) -> str:
        return f"{self.nome} faz um som"

    def apresentar(self) -> str:
        return f"Eu sou {self.nome}. {self.falar()}"


class Gato(Animal):
    def falar(self) -> str:  # sobrescreve o método da classe mãe
        return f"{self.nome}: Miau"


class Cao(Animal):
    def __init__(self, nome: str, raca: str):
        super().__init__(nome)  # aproveita o __init__ de Animal
        self.raca = raca

    def falar(self) -> str:
        return f"{self.nome} ({self.raca}): Au au"


bichos = [Animal("Genérico"), Gato("Mimi"), Cao("Thor", "labrador")]
for bicho in bichos:
    print(bicho.apresentar())  # apresentar() vem de Animal, mas usa o falar() de cada um

print("Thor é um Animal?", isinstance(bichos[2], Animal))
print("Mimi é um Cao?", isinstance(bichos[1], Cao))
