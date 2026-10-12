# Aula 13: 30 exercícios de lógica

O roadmap pede **30 exercícios de lógica resolvidos**. Esta aula não tem teoria nova:
é hora de treinar tudo das aulas 01 a 12 até ficar natural.

## Como fazer

1. A lista está em [exercicios.md](exercicios.md), em ordem crescente de dificuldade.
2. Crie a pasta `aula13/resolvidos/` e **um arquivo por exercício**:
   `ex01.py`, `ex02.py`, …, `ex30.py`. Use o [modelo.py](modelo.py) como ponto de partida.
3. Rode cada um com `python aula13/resolvidos/ex01.py`.
4. Só depois de resolver (ou de travar por pelo menos 20 minutos), compare com a
   solução: `python aula13/solucao.py 1` roda a solução do exercício 1.
5. Marque o exercício como feito na lista.

## Quando travar

1. **Resolva no papel primeiro.** Escreva os passos em português, como uma receita.
2. Teste com números pequenos e confira à mão.
3. Coloque `print()` no meio do código para ver o valor das variáveis a cada passo.
4. Leia a mensagem de erro de baixo para cima (aula 09).
5. Volte ao README da aula indicada entre colchetes no exercício.

## Depois dos 30: Beecrowd

O Beecrowd (<https://judge.beecrowd.com>) é uma plataforma brasileira que corrige seu
código automaticamente. Crie uma conta, filtre a categoria **Iniciante** e comece
pelos problemas de número mais baixo (a partir do 1000).

No Beecrowd:
- **não** escreva mensagens no `input()`. Use só `input()`, porque o corretor
  compara a saída caractere por caractere;
- respeite exatamente o formato de saída pedido (espaços, quebras de linha, casas
  decimais).

```python
# Exemplo no formato Beecrowd: ler dois inteiros (um por linha) e mostrar a soma
a = int(input())
b = int(input())
print(f"X = {a + b}")
```

## Entregável

A pasta `aula13/resolvidos/` com os 30 arquivos. Ela vai para o seu GitHub na
próxima fase do roadmap.
