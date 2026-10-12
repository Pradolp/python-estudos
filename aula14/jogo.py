# Aula 14 - Mini projeto: jogo de adivinhação
# Rode com: python aula14/jogo.py
#
# Implemente as funções na ordem do README. Apague cada "pass" ao implementar.
import random

# Cada dificuldade: (nome, menor número, maior número, tentativas)
DIFICULDADES = {
    "1": ("Fácil", 1, 10, 5),
    "2": ("Médio", 1, 50, 7),
    "3": ("Difícil", 1, 100, 7),
}


def ler_inteiro(mensagem: str, minimo: int, maximo: int) -> int:
    """Pede um inteiro entre minimo e maximo até o usuário digitar um válido."""
    pass


def escolher_dificuldade() -> tuple:
    """Mostra o menu de dificuldades e devolve a tupla escolhida de DIFICULDADES."""
    pass


def calcular_pontos(tentativas_usadas: int, tentativas_max: int, maior: int) -> int:
    """Pontuação de uma vitória: quanto menos tentativas e maior o intervalo, mais pontos.
    Sugestão: (tentativas que sobraram + 1) * maior // tentativas_max"""
    pass


def jogar_rodada(dificuldade: tuple) -> int:
    """Joga uma rodada completa. Devolve os pontos (0 se o jogador perder)."""
    pass


class Placar:
    """Guarda o resultado das partidas: partidas, vitórias e melhor pontuação."""

    pass


def main() -> None:
    """Laço principal: escolhe dificuldade, joga, registra no placar, pergunta se quer repetir."""
    pass


if __name__ == "__main__":
    main()
