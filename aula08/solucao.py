# Aula 08 - Solução (abra só depois de tentar!)


def area_retangulo(largura, altura):
    return largura * altura


def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def eh_primo(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):  # basta testar até a raiz de n
        if n % divisor == 0:
            return False
    return True


def contar_vogais(texto):
    total = 0
    for letra in texto.lower():
        if letra in "aeiouáéíóúâêôãõà":
            total += 1
    return total


def maior_da_lista(numeros):
    if not numeros:
        return None
    maior = numeros[0]
    for n in numeros[1:]:
        if n > maior:
            maior = n
    return maior


def formatar_moeda(valor, simbolo="R$"):
    return f"{simbolo} {valor:.2f}"


def criar_no(valor, esquerda=None, direita=None):
    return {"valor": valor, "esq": esquerda, "dir": direita}


# Exercício 7: inverter_arvore
#
# A ideia central: o filho esquerdo de um nó é uma árvore menor, e o direito
# também. Se a função sabe inverter uma árvore, ela sabe inverter essas duas
# árvores menores. Então ela usa a si mesma para resolver os filhos.
def inverter_arvore(no):
    # Caso base: chegamos "abaixo" de uma folha, onde não há nó nenhum.
    # Sem este if, a função chamaria a si mesma para sempre, até o Python
    # desistir com RecursionError.
    if no is None:
        return None

    # Caso recursivo, tudo numa linha:
    #   - inverter_arvore(no["dir"]) inverte a árvore INTEIRA da direita
    #   - inverter_arvore(no["esq"]) inverte a árvore INTEIRA da esquerda
    #   - a troca da aula 07 coloca a direita invertida na esquerda e
    #     vice-versa
    # Funciona numa linha porque o Python calcula TODO o lado direito do "="
    # antes de guardar qualquer coisa no lado esquerdo.
    no["esq"], no["dir"] = inverter_arvore(no["dir"]), inverter_arvore(no["esq"])

    # Devolver o nó é o que permite a chamada "de cima" receber a árvore
    # invertida e encaixar no lugar certo.
    return no


# A mesma linha da troca, escrita em mais passos:
#
#     esquerda_invertida = inverter_arvore(no["esq"])
#     direita_invertida = inverter_arvore(no["dir"])
#     no["esq"] = direita_invertida
#     no["dir"] = esquerda_invertida
#
# Passo a passo com uma árvore pequena:
#
#       2               2
#      / \    vira     / \
#     1   3           3   1
#
# inverter_arvore(nó 2)
# │   o lado direito do "=" é calculado primeiro:
# ├── inverter_arvore(nó 3)        ← o filho da direita do 2
# │   ├── inverter_arvore(None)  → None  (caso base)
# │   ├── inverter_arvore(None)  → None  (caso base)
# │   └── troca None com None e devolve o nó 3
# ├── inverter_arvore(nó 1)        ← o filho da esquerda do 2
# │   └── igual ao nó 3: devolve o nó 1
# └── guarda: esq = nó 3, dir = nó 1, e devolve o nó 2
#
# Cada chamada fica "em pausa" esperando as chamadas de dentro terminarem. O
# Python guarda essas pausas numa pilha (a "call stack"). Por isso as folhas
# são resolvidas primeiro e a raiz por último.
#
# Para a entrevista: cada nó é visitado uma vez, então o tempo cresce na mesma
# proporção que o número de nós. Em notação de complexidade, isso é O(n).


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
