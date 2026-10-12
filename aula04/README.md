# Aula 04: repetição com `while`

## 1. A ideia

`while` significa "enquanto". O bloco se repete **enquanto a condição for verdadeira**.

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1      # sem esta linha o laço nunca termina!
print("Acabou")
```

Passo a passo: o Python testa `contador <= 5`; se for `True`, roda o bloco e volta
para testar de novo. Quando der `False`, segue para a linha depois do laço.

> **Laço infinito:** se a condição nunca ficar falsa, o programa não para.
> Para interromper no terminal, aperte `Ctrl + C`.

## 2. Os três padrões mais comuns

### a) Contador: repetir um número de vezes

```python
i = 0
while i < 3:
    print("Olá")
    i += 1
```

(Na aula 05 você verá que o `for` é mais prático para isso.)

### b) Sentinela: repetir até o usuário digitar um valor de parada

```python
soma = 0
numero = int(input("Número (0 para sair): "))
while numero != 0:
    soma += numero
    numero = int(input("Número (0 para sair): "))
print("Soma:", soma)
```

### c) Validação: insistir até a entrada ser válida

```python
nota = float(input("Nota (0 a 10): "))
while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Nota (0 a 10): "))
```

## 3. `break` e `continue`

- `break` **sai do laço** na hora.
- `continue` **pula o resto do bloco** e volta para o teste da condição.

```python
while True:                    # laço "infinito" de propósito...
    texto = input("Digite (ou 'sair'): ")
    if texto == "sair":
        break                  # ...que termina com break
    if texto == "":
        continue               # ignora entrada vazia
    print("Você digitou:", texto)
```

O padrão `while True` + `break` é muito usado em menus e jogos, inclusive no
`chat.py` que você vai escrever na fase 4 do roadmap.

## 4. Acumuladores e contadores

Duas variáveis que aparecem em quase todo exercício de laço:

```python
quantidade = 0   # contador: soma 1 a cada volta
total = 0        # acumulador: soma um valor a cada volta
```

Sempre **inicialize antes do laço**. Se a linha `total = 0` ficar dentro do laço, o
total volta a zero a cada repetição.

## Resumo

- `while condição:` repete enquanto a condição for verdadeira.
- Algo dentro do laço precisa mudar a condição, senão ele não termina.
- `break` sai do laço; `continue` pula para a próxima volta.
- `while True` + `break` serve para menus e para repetir "até o usuário pedir para sair".
