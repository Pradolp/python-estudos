# Aula 09 - Exemplos: tratamento de erros
# Rode com: python aula09/exemplos.py

print("=== Provocando cada tipo de erro (e tratando) ===")
testes = [
    ("int('abc')", lambda: int("abc")),
    ("'a' + 1", lambda: "a" + 1),
    ("10 / 0", lambda: 10 / 0),
    ("[1, 2][5]", lambda: [1, 2][5]),
    ("{'a': 1}['b']", lambda: {"a": 1}["b"]),
    ("open('nao_existe.txt')", lambda: open("nao_existe.txt")),
]
# (lambda é uma função de uma linha; aqui serve só para guardar o código e rodar depois)
for codigo, executar in testes:
    try:
        executar()
    except Exception as erro:
        print(f"{codigo:<24} -> {type(erro).__name__}: {erro}")

print("\n=== Vários except ===")


def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print(f"  {a} / {b}: não dá para dividir por zero")
    except TypeError:
        print(f"  {a!r} / {b!r}: os dois precisam ser números")
    else:
        print(f"  {a} / {b} = {resultado}")
    finally:
        print("  (fim da divisão)")


dividir(10, 2)
dividir(10, 0)
dividir("10", 2)

print("\n=== Convertendo uma lista de textos com segurança ===")
entradas = ["10", "7.5", "vinte", "", "42"]
numeros = []
for texto in entradas:
    try:
        numeros.append(float(texto))
    except ValueError:
        print(f"  Ignorando valor inválido: {texto!r}")  # !r mostra com aspas
print("  Números válidos:", numeros)

print("\n=== raise: suas funções recusando dados ruins ===")


def sacar(saldo: float, valor: float) -> float:
    """Devolve o novo saldo. Lança ValueError se o saque for inválido."""
    if valor <= 0:
        raise ValueError("o valor do saque deve ser positivo")
    if valor > saldo:
        raise ValueError(f"saldo insuficiente (saldo: {saldo}, pedido: {valor})")
    return saldo - valor


saldo = 100.0
for pedido in [30, -5, 500, 70]:
    try:
        saldo = sacar(saldo, pedido)
        print(f"  Saque de {pedido}: ok, saldo agora {saldo}")
    except ValueError as erro:
        print(f"  Saque de {pedido}: recusado, {erro}")

print("\n=== Acesso seguro a dicionário: try x get ===")
config = {"modelo": "gemini", "temperatura": 0.7}
try:
    print("  Chave:", config["chave_api"])
except KeyError:
    print("  Com try: chave_api não configurada")
print("  Com get:", config.get("chave_api", "não configurada"))

# --- Padrão de leitura validada (descomente para testar) ---------------------
# def ler_inteiro(mensagem):
#     while True:
#         try:
#             return int(input(mensagem))
#         except ValueError:
#             print("Valor inválido, tente novamente.")
#
# idade = ler_inteiro("Idade: ")
# print("Idade registrada:", idade)
