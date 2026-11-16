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
    return largura * altura


# -----------------------------------------------------------------------------
# Exercício 2: fatorial(n)
# Devolve n! (fatorial de 0 é 1).

def fatorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# -----------------------------------------------------------------------------
# Exercício 3: eh_primo(n)
# Devolve True se n for primo e False se não for.
#%%
def eh_primo(n) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True
print(eh_primo(49))
#%%

# -----------------------------------------------------------------------------
# Exercício 4: contar_vogais(texto)
# Devolve quantas vogais (a, e, i, o, u, com ou sem acento) o texto tem.
# Maiúsculas também contam.
def contar_vogais(texto):
    count = 0
    for letras in texto.lower():
        if letras in "aeiouáéíóúâêôãõà":
            count += 1
    return count

# -----------------------------------------------------------------------------
# Exercício 5: maior_da_lista(numeros)
# Devolve o maior número da lista SEM usar max().
# Se a lista estiver vazia, devolve None.
#%%
def maior_da_lista(numeros):
    if not numeros:
        return None
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior
print(maior_da_lista([2,4,5]))
#%%

# -----------------------------------------------------------------------------
# Exercício 6: formatar_moeda(valor, simbolo="R$")
# Devolve o valor como texto com 2 casas decimais: formatar_moeda(5) -> "R$ 5.00"
def formatar_moeda(valor, simbolo="R$"):
    pass


# -----------------------------------------------------------------------------
# Exercício 7 (desafio de entrevista): inverter_arvore(no)
# Numa árvore binária, cada "nó" tem um valor e até dois filhos: um à esquerda
# ("esq") e um à direita ("dir"). Aqui cada nó é um dicionário. Quando não há
# filho, o valor é None. A função criar_no, logo abaixo, já está pronta: ela só
# monta esse dicionário para você.
#
# Inverter a árvore é trocar esquerda e direita em TODOS os nós (como um
# espelho). A função deve inverter a árvore e devolver o nó que recebeu.
#
#          4                         4
#        /   \                     /   \
#       2     7       vira        7     2
#      / \   / \                 / \   / \
#     1   3 6   9               9   6 3   1
#
# Recursão: uma função pode chamar a si mesma. Repare que o filho esquerdo de
# um nó também é uma árvore, só que menor. O direito também. Então, para
# inverter uma árvore:
#   1. inverta a árvore da esquerda (chamando inverter_arvore nela)
#   2. inverta a árvore da direita (do mesmo jeito)
#   3. troque as duas de lugar: a, b = b, a
# Toda recursão precisa de um ponto de parada, o "caso base". Sem ele, a função
# chama a si mesma para sempre. Aqui: se o nó for None, não há o que inverter.
#
# É o problema 226 do LeetCode ("Invert Binary Tree").
def criar_no(valor, esquerda=None, direita=None):
    return {"valor": valor, "esq": esquerda, "dir": direita}


def inverter_arvore(no):
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
assert contar_vogais("Inteligência Artificial") == 11
assert maior_da_lista([3, 9, 2]) == 9
assert maior_da_lista([-5, -2, -8]) == -2
assert maior_da_lista([]) is None
assert formatar_moeda(5) == "R$ 5.00"
assert formatar_moeda(3.14159, "US$") == "US$ 3.14"
arvore = criar_no(4,
                  criar_no(2, criar_no(1), criar_no(3)),
                  criar_no(7, criar_no(6), criar_no(9)))
espelho = criar_no(4,
                   criar_no(7, criar_no(9), criar_no(6)),
                   criar_no(2, criar_no(3), criar_no(1)))
assert inverter_arvore(arvore) == espelho
assert inverter_arvore(criar_no(5)) == criar_no(5)
assert inverter_arvore(None) is None
print("Todos os testes passaram!")
