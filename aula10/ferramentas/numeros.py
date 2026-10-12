"""Funções para trabalhar com números."""


def eh_par(n: int) -> bool:
    """Diz se n é par."""
    return n % 2 == 0


def media(valores: list) -> float:
    """Média de uma lista de números. Lança ValueError se a lista estiver vazia."""
    if not valores:
        raise ValueError("não é possível calcular a média de uma lista vazia")
    return sum(valores) / len(valores)


if __name__ == "__main__":
    # Só roda se você executar este arquivo diretamente:
    #   python aula10/ferramentas/numeros.py
    print("Testando numeros.py")
    print("eh_par(4):", eh_par(4))
    print("media([1, 2, 3]):", media([1, 2, 3]))
