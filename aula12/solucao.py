# Aula 12 - Solução (abra só depois de tentar!)


# Exercício 1
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def eh_quadrado(self):
        return self.largura == self.altura

    def __str__(self):
        return f"Retângulo {self.largura}x{self.altura}"


# Exercício 2
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho:
    def __init__(self):
        self.itens = []  # lista de tuplas (produto, quantidade)

    def adicionar(self, produto, quantidade=1):
        if quantidade < 1:
            raise ValueError("a quantidade deve ser pelo menos 1")
        self.itens.append((produto, quantidade))

    def total(self):
        return sum(produto.preco * qtd for produto, qtd in self.itens)

    def quantidade_itens(self):
        return sum(qtd for _, qtd in self.itens)


# Exercício 3
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, salario, tamanho_equipe):
        super().__init__(nome, salario)
        self.tamanho_equipe = tamanho_equipe

    def bonus(self):
        return self.salario * 0.20 + 100 * self.tamanho_equipe


r = Retangulo(3, 4)
assert r.area() == 12
assert r.perimetro() == 14
assert r.eh_quadrado() is False
assert Retangulo(5, 5).eh_quadrado() is True
assert str(r) == "Retângulo 3x4"
print("Exercício 1 ok!")

carrinho = Carrinho()
carrinho.adicionar(Produto("Caneta", 2.50), 4)
carrinho.adicionar(Produto("Caderno", 15.00))
assert carrinho.total() == 25.0
assert carrinho.quantidade_itens() == 5
try:
    carrinho.adicionar(Produto("Borracha", 1.0), 0)
    assert False, "deveria ter lançado ValueError"
except ValueError:
    pass
print("Exercício 2 ok!")

f = Funcionario("Ana", 3000)
g = Gerente("Bruno", 8000, tamanho_equipe=5)
assert f.bonus() == 300
assert g.bonus() == 2100
assert g.nome == "Bruno" and isinstance(g, Funcionario)
print("Exercício 3 ok!")
