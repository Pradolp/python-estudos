# Aula 14 - Solução do mini projeto (abra só depois de tentar!)
# Inclui os desafios extras: dica de "quente", palpites anteriores e recorde salvo em arquivo.
import json
import random
from pathlib import Path

DIFICULDADES = {
    "1": ("Fácil", 1, 10, 5),
    "2": ("Médio", 1, 50, 7),
    "3": ("Difícil", 1, 100, 7),
}
ARQUIVO_RECORDE = Path(__file__).parent / "recorde.json"


def ler_inteiro(mensagem: str, minimo: int, maximo: int) -> int:
    """Pede um inteiro entre minimo e maximo até o usuário digitar um válido."""
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("  Digite um número inteiro.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"  Digite um número entre {minimo} e {maximo}.")


def escolher_dificuldade() -> tuple:
    """Mostra o menu de dificuldades e devolve a tupla escolhida de DIFICULDADES."""
    print("Escolha a dificuldade:")
    for opcao, (nome, menor, maior, tentativas) in DIFICULDADES.items():
        print(f"  [{opcao}] {nome:<8}({menor} a {maior}, {tentativas} tentativas)")
    while True:
        opcao = input("Opção: ").strip()
        if opcao in DIFICULDADES:
            return DIFICULDADES[opcao]
        print("  Opção inválida.")


def calcular_pontos(tentativas_usadas: int, tentativas_max: int, maior: int) -> int:
    """Pontuação de uma vitória: quanto menos tentativas e maior o intervalo, mais pontos."""
    sobraram = tentativas_max - tentativas_usadas
    return (sobraram + 1) * maior // tentativas_max


def jogar_rodada(dificuldade: tuple) -> int:
    """Joga uma rodada completa. Devolve os pontos (0 se o jogador perder)."""
    nome, menor, maior, tentativas_max = dificuldade
    secreto = random.randint(menor, maior)
    palpites = []
    print(f"\nPensei num número de {menor} a {maior}. Você tem {tentativas_max} tentativas.")

    for tentativa in range(1, tentativas_max + 1):
        palpite = ler_inteiro(f"Tentativa {tentativa}/{tentativas_max}: ", menor, maior)
        palpites.append(palpite)
        if palpite == secreto:
            pontos = calcular_pontos(tentativa, tentativas_max, maior)
            print(f"  Acertou em {tentativa} tentativa(s)! Pontos: {pontos}")
            return pontos
        direcao = "MAIOR" if secreto > palpite else "MENOR"
        dica = "  (está quente!)" if abs(secreto - palpite) <= 3 else ""
        print(f"  O número é {direcao} que {palpite}.{dica}")
        print(f"  Palpites: {palpites}")

    print(f"  Suas tentativas acabaram. O número era {secreto}.")
    return 0


class Placar:
    """Guarda o resultado das partidas e o recorde salvo em arquivo."""

    def __init__(self, arquivo: Path):
        self.arquivo = arquivo
        self.partidas = 0
        self.vitorias = 0
        self.melhor = 0
        self.recorde = self._carregar_recorde()

    def _carregar_recorde(self) -> int:
        try:
            return json.loads(self.arquivo.read_text(encoding="utf-8"))["recorde"]
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return 0

    def registrar(self, pontos: int) -> None:
        self.partidas += 1
        if pontos > 0:
            self.vitorias += 1
        self.melhor = max(self.melhor, pontos)
        if pontos > self.recorde:
            self.recorde = pontos
            self.arquivo.write_text(json.dumps({"recorde": pontos}), encoding="utf-8")
            print("  NOVO RECORDE!")

    def __str__(self) -> str:
        return (
            f"Partidas: {self.partidas} | Vitórias: {self.vitorias} | "
            f"Melhor pontuação: {self.melhor} | Recorde geral: {self.recorde}"
        )


def main() -> None:
    """Laço principal: escolhe dificuldade, joga, registra no placar, pergunta se quer repetir."""
    print("=== JOGO DE ADIVINHAÇÃO ===")
    placar = Placar(ARQUIVO_RECORDE)
    while True:
        dificuldade = escolher_dificuldade()
        placar.registrar(jogar_rodada(dificuldade))
        if input("\nJogar de novo? [S/N] ").strip().upper() != "S":
            break
    print("\n=== PLACAR ===")
    print(placar)
    print("Até a próxima!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:  # Ctrl+C: sai sem mostrar traceback
        print("\nJogo interrompido. Até a próxima!")
