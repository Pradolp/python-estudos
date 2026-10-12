# Aula 03: decisões com `if`, `elif` e `else`

## 1. A estrutura básica

```python
idade = int(input("Idade: "))

if idade >= 18:
    print("Pode dirigir.")
else:
    print("Ainda não pode dirigir.")

print("Fim")  # fora do if: sempre executa
```

Três detalhes que o Python exige:

1. **Dois-pontos** `:` no fim da linha do `if` e do `else`.
2. **Indentação** (recuo de 4 espaços) no bloco de dentro. É ela que diz ao Python
   o que pertence ao `if`. O VS Code coloca o recuo sozinho quando você aperta Enter
   depois do `:`.
3. O `else` é opcional.

## 2. Várias possibilidades: `elif`

`elif` significa "senão, se". O Python testa de cima para baixo e executa **só o
primeiro** bloco cuja condição for verdadeira.

```python
nota = 7.5

if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"      # entra aqui e pula o resto
elif nota >= 5:
    conceito = "C"
else:
    conceito = "D"
```

> A ordem importa. Se o teste `nota >= 5` viesse primeiro, uma nota 9.5 cairia nele.

## 3. Condições compostas

Use `and`, `or` e `not` da aula 02:

```python
if idade >= 16 and idade < 18:
    print("Voto opcional")

if dia == "sábado" or dia == "domingo":
    print("Fim de semana")

if dia in ("sábado", "domingo"):   # forma mais curta para o caso acima
    print("Fim de semana")
```

## 4. `if` dentro de `if` (aninhado)

```python
if tem_cadastro:
    if senha_correta:
        print("Bem-vindo!")
    else:
        print("Senha errada.")
else:
    print("Faça seu cadastro.")
```

Quando o aninhamento fica profundo demais, normalmente dá para simplificar com `and`
ou `elif`.

## 5. Valores "verdadeiros" e "falsos"

O `if` aceita qualquer valor, não só `True`/`False`. São considerados **falsos**:
`0`, `0.0`, `""` (texto vazio), `[]` (lista vazia), `None`. Todo o resto é verdadeiro.

```python
nome = input("Nome: ")
if nome:              # mesmo que: if nome != "":
    print(f"Olá, {nome}")
else:
    print("Você não digitou nada.")
```

## 6. `if` em uma linha (expressão condicional)

Para escolher entre dois valores:

```python
situacao = "aprovado" if nota >= 7 else "reprovado"
```

## 7. `match` (bônus)

A partir do Python 3.10 existe o `match`, útil para comparar um valor com várias
opções fixas:

```python
match opcao:
    case "1":
        print("Somar")
    case "2":
        print("Subtrair")
    case _:            # _ = qualquer outro valor
        print("Opção inválida")
```

## Resumo

- `if condição:` + bloco com recuo de 4 espaços.
- `elif` testa outras condições em ordem; só o primeiro bloco verdadeiro roda.
- `else` pega tudo o que sobrou.
- `0`, `""`, `[]` e `None` contam como falso.
