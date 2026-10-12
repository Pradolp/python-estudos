# Aula 08 - Exercícios
# Rode com: python aula08/exercicio.py
#
# Escreva cada função no lugar indicado. Os testes no fim do arquivo usam
# assert: se a função estiver certa, nada acontece; se estiver errada, o
# programa para e mostra AssertionError na linha do teste que falhou.
# Quando todos passarem você verá "Todos os testes passaram!".


# -----------------------------------------------------------------------------
# Exercício 1: area_retangulo(largura, altura)
# Devolve a área do retângulo.
def area_retangulo(largura, altura):
    pass  # apague o pass e escreva seu código


# -----------------------------------------------------------------------------
# Exercício 2: fatorial(n)
# Devolve n! (fatorial de 0 é 1).
def fatorial(n):
    pass


# -----------------------------------------------------------------------------
# Exercício 3: eh_primo(n)
# Devolve True se n for primo e False se não for.
def eh_primo(n):
    pass


# -----------------------------------------------------------------------------
# Exercício 4: contar_vogais(texto)
# Devolve quantas vogais (a, e, i, o, u, com ou sem acento) o texto tem.
# Maiúsculas também contam.
def contar_vogais(texto):
    pass


# -----------------------------------------------------------------------------
# Exercício 5: maior_da_lista(numeros)
# Devolve o maior número da lista SEM usar max().
# Se a lista estiver vazia, devolve None.
def maior_da_lista(numeros):
    pass


# -----------------------------------------------------------------------------
# Exercício 6: formatar_moeda(valor, simbolo="R$")
# Devolve o valor como texto com 2 casas decimais: formatar_moeda(5) -> "R$ 5.00"
def formatar_moeda(valor, simbolo="R$"):
    pass


# -----------------------------------------------------------------------------
# Testes (não mexa daqui para baixo)
assert area_retangulo(3, 4) == 12
assert area_retangulo(2.5, 2) == 5
assert fatorial(0) == 1
assert fatorial(5) == 120
assert eh_primo(2) is True
assert eh_primo(17) is True
assert eh_primo(1) is False
assert eh_primo(15) is False
assert contar_vogais("Python") == 1
assert contar_vogais("Inteligência Artificial") == 10
assert maior_da_lista([3, 9, 2]) == 9
assert maior_da_lista([-5, -2, -8]) == -2
assert maior_da_lista([]) is None
assert formatar_moeda(5) == "R$ 5.00"
assert formatar_moeda(3.14159, "US$") == "US$ 3.14"
print("Todos os testes passaram!")
