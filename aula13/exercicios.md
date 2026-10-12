# Os 30 exercícios

Entre colchetes está a aula onde o assunto foi explicado. Marque com `x` os que
terminar: `- [x]`.

## Bloco 1: sequencial (entrada, conta, saída)

- [ ] **01. Soma** [01] Leia dois números inteiros e mostre a soma.
  `5` e `7` → `A soma é 12`
- [ ] **02. Média** [01] Leia três notas e mostre a média com 1 casa decimal.
- [ ] **03. Metros** [02] Leia uma distância em metros e mostre em centímetros e em
  milímetros.
- [ ] **04. Aumento** [02] Leia um salário e mostre o novo salário com 15% de aumento.
- [ ] **05. Círculo** [10] Leia o raio de um círculo e mostre a área (`π × r²`) com 2
  casas. Use `math.pi`.
- [ ] **06. Relógio** [02] Leia uma quantidade de segundos e mostre no formato
  `horas:minutos:segundos`. `3725` → `1:2:5`

## Bloco 2: condicionais

- [ ] **07. Maior** [03] Leia dois números e diga qual é o maior, ou se são iguais.
- [ ] **08. Sinal** [03] Leia um número e diga se é positivo, negativo ou zero.
- [ ] **09. Triângulo** [03] Leia três lados. Diga se formam um triângulo (cada lado
  menor que a soma dos outros dois) e, se formarem, se ele é equilátero, isósceles
  ou escaleno.
- [ ] **10. Empréstimo** [03] Leia o valor de uma casa, o salário do comprador e em
  quantos anos ele vai pagar. A prestação mensal não pode passar de 30% do salário.
  Diga se o empréstimo foi aprovado.
- [ ] **11. Natação** [03] Leia o ano de nascimento de um atleta e mostre a
  categoria: até 9 anos *Mirim*, até 14 *Infantil*, até 19 *Júnior*, até 25
  *Sênior*, acima *Master*.
- [ ] **12. IMC completo** [03] Leia peso e altura, calcule o IMC e mostre a faixa:
  abaixo de 18.5 *abaixo do peso*, até 25 *normal*, até 30 *sobrepeso*, acima
  *obesidade*.
- [ ] **13. Bhaskara** [03] Leia a, b e c de `ax² + bx + c = 0`. Calcule o delta.
  Se for negativo, diga que não há raízes reais; senão, mostre as raízes.

## Bloco 3: laços

- [ ] **14. Contagem** [05] Leia N e mostre os números de 1 até N na mesma linha.
- [ ] **15. Ímpares múltiplos de 3** [05] Mostre a soma de todos os números ímpares
  que são múltiplos de 3 entre 1 e 500, e quantos são.
- [ ] **16. Todas as tabuadas** [05] Mostre as tabuadas do 1 ao 10 (laço dentro de
  laço).
- [ ] **17. Divisores** [05] Leia um número e mostre todos os seus divisores e
  quantos são. Diga se é primo.
- [ ] **18. Progressão aritmética** [04] Leia o primeiro termo e a razão de uma PA e
  mostre os 10 primeiros termos. Depois pergunte quantos termos a mais o usuário
  quer ver, até ele digitar 0.
- [ ] **19. Par ou ímpar** [04/10] Jogue par ou ímpar contra o computador
  (`random.randint(0, 10)`). O jogo só para quando o jogador perder. Mostre
  quantas vezes ele venceu seguidas.
- [ ] **20. Número perfeito** [05] Um número é perfeito quando é igual à soma dos
  seus divisores menores que ele (6 = 1 + 2 + 3). Mostre todos os perfeitos de 1
  a 10000.
- [ ] **21. Estatísticas** [04] Leia números até o usuário digitar `fim`. Mostre
  quantos foram, a soma, a média, o maior e o menor.

## Bloco 4: listas e strings

- [ ] **22. Inverter** [06] Leia 6 números para uma lista e mostre a lista invertida
  **sem** usar `reverse()` nem `[::-1]`.
- [ ] **23. Palavras** [02/06] Leia uma frase e mostre quantas palavras ela tem, a
  maior palavra e a frase com as palavras em ordem alfabética.
- [ ] **24. Sem vogais** [05] Leia uma frase e mostre a mesma frase sem as vogais.
- [ ] **25. Segundo maior** [06] Dada uma lista de números (pode ter repetidos), mostre
  o segundo maior valor **diferente**. `[5, 9, 3, 9, 7]` → `7`
- [ ] **26. Juntar ordenado** [06] Dadas duas listas já ordenadas, crie uma terceira
  lista ordenada com todos os itens **sem** usar `sort()` nem `sorted()`.
  `[1, 4, 7]` e `[2, 3, 8]` → `[1, 2, 3, 4, 7, 8]`

## Bloco 5: dicionários, funções e erros

- [ ] **27. Top 3 palavras** [07] Leia um texto e mostre as 3 palavras que mais
  aparecem e quantas vezes cada uma aparece (ignore maiúsculas e pontuação `.,!?`).
- [ ] **28. Caixa eletrônico** [07/08] Crie a função `sacar_notas(valor)` que devolve
  um dicionário com quantas notas de 100, 50, 20, 10, 5 e 2 são necessárias, usando
  o menor número de notas. Se o valor não puder ser pago (ex.: 3), lance
  `ValueError`. `180` → `{100: 1, 50: 1, 20: 1, 10: 1}`
- [ ] **29. Agenda** [07/09] Agenda telefônica com dicionário e menu: adicionar
  contato, buscar pelo nome, listar todos em ordem alfabética, remover e sair.
  Trate nomes que não existem.
- [ ] **30. Senha forte** [08] Crie a função `validar_senha(senha)` que devolve uma
  lista com os problemas da senha (lista vazia = senha forte). Regras: pelo menos 8
  caracteres, uma letra maiúscula, uma minúscula, um número e um símbolo
  (algo que não seja letra nem número). Dica: `c.isupper()`, `c.islower()`,
  `c.isdigit()`, `c.isalnum()`.
