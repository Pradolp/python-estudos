"""Solução do exercício 3 da aula 10: módulo de conversões."""


def celsius_para_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def km_para_milhas(km: float) -> float:
    return km * 0.621371


def reais_para_dolar(valor: float, cotacao: float) -> float:
    return valor / cotacao


if __name__ == "__main__":
    print(celsius_para_fahrenheit(100))  # 212.0
    print(km_para_milhas(10))            # 6.21371
    print(reais_para_dolar(540, 5.40))   # 100.0
