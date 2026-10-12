# Aula 12 - Exercícios
# Rode com: python aula12/exercicio.py
# Os testes no fim do arquivo verificam suas classes (como na aula 08).


# -----------------------------------------------------------------------------
# Exercício 1: Retangulo
# Crie a classe Retangulo com:
#   - __init__(self, largura, altura)
#   - area(self)       -> largura * altura
#   - perimetro(self)  -> 2 * (largura + altura)
#   - eh_quadrado(self) -> True se largura == altura
#   - __str__(self)    -> "Retângulo 3x4"
# Escreva seu código aqui:



# -----------------------------------------------------------------------------
# Exercício 2: Produto e Carrinho
# a) Classe Produto com nome e preco.
# b) Classe Carrinho com:
#    - __init__(self): começa com uma lista vazia de itens
#    - adicionar(self, produto, quantidade=1)
#      (lance ValueError se a quantidade for menor que 1)
#    - total(self) -> soma de preço x quantidade de todos os itens
#    - quantidade_itens(self) -> soma de todas as quantidades
# Dica: guarde cada item como uma tupla (produto, quantidade).
# Escreva seu código aqui:



# -----------------------------------------------------------------------------
# Exercício 3: Funcionários (herança)
# a) Classe Funcionario com nome e salario, e método bonus() que devolve 10%
#    do salário.
# b) Classe Gerente que herda de Funcionario, recebe também o tamanho_equipe e
#    sobrescreve bonus(): 20% do salário + 100 por pessoa na equipe.
#    Use super().__init__ no construtor.
# Escreva seu código aqui:



# -----------------------------------------------------------------------------
# Testes. Descomente cada bloco quando terminar o exercício correspondente.

# r = Retangulo(3, 4)
# assert r.area() == 12
# assert r.perimetro() == 14
# assert r.eh_quadrado() is False
# assert Retangulo(5, 5).eh_quadrado() is True
# assert str(r) == "Retângulo 3x4"
# print("Exercício 1 ok!")

# carrinho = Carrinho()
# carrinho.adicionar(Produto("Caneta", 2.50), 4)
# carrinho.adicionar(Produto("Caderno", 15.00))
# assert carrinho.total() == 25.0
# assert carrinho.quantidade_itens() == 5
# try:
#     carrinho.adicionar(Produto("Borracha", 1.0), 0)
#     assert False, "deveria ter lançado ValueError"
# except ValueError:
#     pass
# print("Exercício 2 ok!")

# f = Funcionario("Ana", 3000)
# g = Gerente("Bruno", 8000, tamanho_equipe=5)
# assert f.bonus() == 300
# assert g.bonus() == 2100
# assert g.nome == "Bruno" and isinstance(g, Funcionario)
# print("Exercício 3 ok!")
