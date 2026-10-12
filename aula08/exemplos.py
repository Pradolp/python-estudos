# Aula 08 - Exemplos: funções
# Rode com: python aula08/exemplos.py


def linha(tamanho=30, simbolo="="):
    """Mostra uma linha separadora."""
    print(simbolo * tamanho)


def somar(a, b):
    return a + b


def eh_par(n: int) -> bool:
    """Diz se n é par."""
    return n % 2 == 0


def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o IMC (peso em kg, altura em metros)."""
    return peso / altura ** 2


def classificar_imc(imc: float) -> str:
    """Devolve a faixa do IMC segundo a OMS."""
    if imc < 18.5:
        return "abaixo do peso"   # o return encerra a função aqui
    if imc < 25:
        return "peso normal"
    if imc < 30:
        return "sobrepeso"
    return "obesidade"


def estatisticas(numeros: list) -> tuple:
    """Devolve (menor, maior, média) de uma lista de números."""
    return min(numeros), max(numeros), sum(numeros) / len(numeros)


def cumprimentar(nome, saudacao="Olá", pontuacao="!"):
    return f"{saudacao}, {nome}{pontuacao}"


def somar_tudo(*numeros):
    """Soma quantos números forem passados."""
    total = 0
    for n in numeros:
        total += n
    return total


def mostrar_dobro(n):
    print(n * 2)  # sem return: a função devolve None


linha()
print("Funções básicas")
linha()
print("somar(3, 4) =", somar(3, 4))
print("somar('Py', 'thon') =", somar("Py", "thon"))  # funciona com qualquer coisa que aceite +
print("eh_par(10) =", eh_par(10))
print("eh_par(7) =", eh_par(7))

linha(simbolo="-")
print("Uma função usando outra")
imc = calcular_imc(70, 1.75)
print(f"IMC: {imc:.2f} -> {classificar_imc(imc)}")

linha(simbolo="-")
print("Devolvendo vários valores")
menor, maior, media = estatisticas([7, 3, 9, 5])
print(f"Menor {menor}, maior {maior}, média {media}")

linha(simbolo="-")
print("Valores padrão e argumentos nomeados")
print(cumprimentar("Ana"))
print(cumprimentar("Ana", "Bom dia"))
print(cumprimentar(pontuacao="?", nome="Bruno", saudacao="Tudo bem"))

linha(simbolo="-")
print("*args")
print(somar_tudo(1, 2, 3))
print(somar_tudo(10, 20, 30, 40, 50))

linha(simbolo="-")
print("print x return")
resultado = mostrar_dobro(5)
print("O que mostrar_dobro devolveu:", resultado)

linha(simbolo="-")
print("Docstring (o texto que o VS Code e os agentes de IA leem):")
print(calcular_imc.__doc__)

linha(simbolo="-")
print("Escopo")
contador = 0


def tentar_mudar():
    contador = 100  # cria uma variável LOCAL com o mesmo nome; a de fora não muda
    return contador


print("Dentro da função:", tentar_mudar())
print("Fora da função:", contador)
