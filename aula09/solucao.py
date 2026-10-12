# Aula 09 - Solução (abra só depois de tentar!)


# Exercício 1
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido")


numero = ler_inteiro("Número inteiro: ")
print("Você digitou", numero)


# Exercício 2
def ler_float_intervalo(mensagem, minimo, maximo):
    while True:
        try:
            valor = float(input(mensagem))
        except ValueError:
            print("Digite um número.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"O valor deve estar entre {minimo} e {maximo}.")


nota = ler_float_intervalo("Nota (0 a 10): ", 0, 10)
print("Nota registrada:", nota)

# Exercício 3
try:
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
except ValueError:
    print("Número inválido.")
else:
    operacao = input("Operação (+ - * /): ").strip()
    try:
        if operacao == "+":
            print(a + b)
        elif operacao == "-":
            print(a - b)
        elif operacao == "*":
            print(a * b)
        elif operacao == "/":
            print(a / b)
        else:
            print("Operação desconhecida.")
    except ZeroDivisionError:
        print("Não dá para dividir por zero.")


# Exercício 4
def criar_usuario(nome, idade):
    nome = nome.strip()
    if not nome:
        raise ValueError("o nome não pode ficar vazio")
    if idade < 0 or idade > 150:
        raise ValueError(f"idade inválida: {idade}")
    return {"nome": nome, "idade": idade}


for nome, idade in [("Ana", 30), ("   ", 20), ("Bruno", -3), ("Carla", 200)]:
    try:
        usuario = criar_usuario(nome, idade)
        print("Criado:", usuario)
    except ValueError as erro:
        print(f"Erro ao criar ({nome!r}, {idade}): {erro}")

# Exercício 5
cores = ["vermelho", "verde", "azul", "amarelo"]
try:
    posicao = int(input(f"Posição (0 a {len(cores) - 1}): "))
    print("Cor:", cores[posicao])
except ValueError:
    print("Digite um número inteiro.")
except IndexError:
    print("Essa posição não existe.")
