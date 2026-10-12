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
print("Todos os testes passaram!")
