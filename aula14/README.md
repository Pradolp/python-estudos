# Aula 14: mini projeto, jogo de adivinhação

Último passo da fase "Python do zero". Você vai construir um programa completo que
usa **tudo** o que aprendeu: variáveis, `if`, laços, listas, dicionários, funções,
`try/except`, módulos e uma classe.

## O jogo

O computador sorteia um número secreto e o jogador tenta adivinhar. A cada palpite
o jogo diz se o número secreto é **maior** ou **menor**.

```
=== JOGO DE ADIVINHAÇÃO ===
Escolha a dificuldade:
  [1] Fácil   (1 a 10,  5 tentativas)
  [2] Médio   (1 a 50,  7 tentativas)
  [3] Difícil (1 a 100, 7 tentativas)
Opção: 2

Pensei num número de 1 a 50. Você tem 7 tentativas.
Tentativa 1/7: 25
  O número é MENOR que 25.
Tentativa 2/7: abc
  Digite um número inteiro.
Tentativa 2/7: 12
  O número é MAIOR que 12.  (está quente!)
Tentativa 3/7: 15
  Acertou em 3 tentativas! Pontos: 71

Jogar de novo? [S/N] n

=== PLACAR ===
Partidas: 1 | Vitórias: 1 | Melhor pontuação: 71
Até a próxima!
```

## Requisitos

Funcionais (o que o jogo faz):

1. Menu com 3 dificuldades, cada uma com intervalo e número de tentativas próprios.
2. Sortear o número com `random.randint`.
3. A cada palpite, dizer se o secreto é maior ou menor.
4. Entradas inválidas (texto, número fora do intervalo) **não** gastam tentativa e
   **não** derrubam o programa.
5. Ao acertar, mostrar em quantas tentativas e a pontuação. Ao perder, revelar o número.
6. Perguntar se quer jogar de novo.
7. No fim, mostrar um placar com partidas, vitórias e melhor pontuação.

Técnicos (como o código deve ser):

- Dificuldades guardadas num **dicionário** (nada de `if` para cada nível espalhado
  pelo código).
- Código dividido em **funções** pequenas, cada uma fazendo uma coisa só.
- O placar é uma **classe** `Placar`.
- O jogo começa num bloco `if __name__ == "__main__":`.

## Por onde começar

O arquivo [jogo.py](jogo.py) já tem o **esqueleto**: as funções existem, com
docstring explicando o que cada uma faz, mas o corpo está vazio. Implemente uma
por vez, nesta ordem, testando a cada passo:

1. `ler_inteiro` (reaproveite a ideia da aula 09)
2. `escolher_dificuldade`
3. `calcular_pontos`
4. `jogar_rodada`
5. a classe `Placar`
6. `main`

Rode com:

```bash
python aula14/jogo.py
```

A versão completa está em [solucao.py](solucao.py). Abra só para comparar no fim.

## Desafios extras (opcionais)

- Dica de "quente" quando o palpite estiver a no máximo 3 de distância do número.
- Mostrar os palpites já feitos naquela rodada.
- Salvar o recorde num arquivo `recorde.json` para ele sobreviver entre execuções
  (módulo `json` + `pathlib`, aula 10).
- Modo inverso: **você** pensa num número e o computador tenta adivinhar
  (dica: busca binária, sempre chutando o meio do intervalo).

## Alternativa: calculadora no terminal

O roadmap aceita "jogo de adivinhação **ou** calculadora". Se preferir, faça
também uma calculadora com:

- menu em loop com soma, subtração, multiplicação, divisão, potência e raiz;
- histórico das operações (lista) que pode ser exibido;
- tratamento de entradas inválidas e divisão por zero;
- uma função por operação, guardadas num dicionário `{"+": somar, "-": subtrair, ...}`.

## Entregável

Com o jogo rodando, você concluiu a fase **Python do zero**. Marque as tarefas no
roadmap e siga para a fase **Git, GitHub e terminal**, onde esta pasta vira o seu
primeiro repositório publicado.
