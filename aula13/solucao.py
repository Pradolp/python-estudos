# Aula 13 - Soluções dos 30 exercícios (abra só depois de tentar!)
# Rode uma solução específica com:  python aula13/solucao.py 7
import math
import random
import sys


def ex01():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"A soma é {a + b}")


def ex02():
    n1, n2, n3 = (float(input(f"Nota {i}: ")) for i in range(1, 4))
    print(f"Média: {(n1 + n2 + n3) / 3:.1f}")


def ex03():
    metros = float(input("Metros: "))
    print(f"{metros} m = {metros * 100} cm = {metros * 1000} mm")


def ex04():
    salario = float(input("Salário: R$ "))
    print(f"Novo salário: R$ {salario * 1.15:.2f}")


def ex05():
    raio = float(input("Raio: "))
    print(f"Área: {math.pi * raio ** 2:.2f}")


def ex06():
    total = int(input("Segundos: "))
    print(f"{total // 3600}:{total % 3600 // 60}:{total % 60}")


def ex07():
    a = float(input("A: "))
    b = float(input("B: "))
    if a > b:
        print("O primeiro é maior")
    elif b > a:
        print("O segundo é maior")
    else:
        print("São iguais")


def ex08():
    n = float(input("Número: "))
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("Zero")


def ex09():
    a, b, c = (float(input(f"Lado {i}: ")) for i in range(1, 4))
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            tipo = "equilátero"
        elif a == b or b == c or a == c:
            tipo = "isósceles"
        else:
            tipo = "escaleno"
        print(f"Forma um triângulo {tipo}")
    else:
        print("Não forma um triângulo")


def ex10():
    casa = float(input("Valor da casa: R$ "))
    salario = float(input("Salário: R$ "))
    anos = int(input("Anos para pagar: "))
    prestacao = casa / (anos * 12)
    print(f"Prestação: R$ {prestacao:.2f}")
    if prestacao <= salario * 0.30:
        print("Empréstimo APROVADO")
    else:
        print("Empréstimo NEGADO (passa de 30% do salário)")


def ex11():
    from datetime import date

    idade = date.today().year - int(input("Ano de nascimento: "))
    if idade <= 9:
        categoria = "Mirim"
    elif idade <= 14:
        categoria = "Infantil"
    elif idade <= 19:
        categoria = "Júnior"
    elif idade <= 25:
        categoria = "Sênior"
    else:
        categoria = "Master"
    print(f"{idade} anos: categoria {categoria}")


def ex12():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / altura ** 2
    if imc < 18.5:
        faixa = "abaixo do peso"
    elif imc < 25:
        faixa = "normal"
    elif imc < 30:
        faixa = "sobrepeso"
    else:
        faixa = "obesidade"
    print(f"IMC {imc:.1f}: {faixa}")


def ex13():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    if a == 0:
        print("'a' não pode ser zero numa equação do 2º grau")
        return
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print(f"Delta = {delta}: não há raízes reais")
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"Delta = {delta} | x1 = {x1} | x2 = {x2}")


def ex14():
    n = int(input("N: "))
    for i in range(1, n + 1):
        print(i, end=" ")
    print()


def ex15():
    soma = quantidade = 0
    for n in range(3, 501, 6):  # 3, 9, 15... (ímpares múltiplos de 3 pulam de 6 em 6)
        soma += n
        quantidade += 1
    print(f"{quantidade} números, soma {soma}")


def ex16():
    for tabuada in range(1, 11):
        print(f"--- Tabuada do {tabuada} ---")
        for i in range(1, 11):
            print(f"{tabuada} x {i} = {tabuada * i}")


def ex17():
    n = int(input("Número: "))
    divisores = [d for d in range(1, n + 1) if n % d == 0]
    print("Divisores:", divisores, f"({len(divisores)})")
    print("É primo" if len(divisores) == 2 else "Não é primo")


def ex18():
    termo = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    mais = 10
    mostrados = 0
    while mais > 0:
        for _ in range(mais):
            print(termo, end=" → ")
            termo += razao
        mostrados += mais
        print("PAUSA")
        mais = int(input("Quantos termos a mais? (0 para sair) "))
    print(f"Total de termos mostrados: {mostrados}")


def ex19():
    vitorias = 0
    while True:
        jogador = int(input("Seu número: "))
        escolha = ""
        while escolha not in ("P", "I"):
            escolha = input("Par ou ímpar? [P/I] ").strip().upper()
        computador = random.randint(0, 10)
        total = jogador + computador
        resultado = "P" if total % 2 == 0 else "I"
        print(f"Você {jogador} + computador {computador} = {total}")
        if resultado == escolha:
            vitorias += 1
            print("Você venceu! Vamos de novo.")
        else:
            print(f"Você perdeu! Vitórias seguidas: {vitorias}")
            break


def ex20():
    for n in range(2, 10001):
        soma = 1  # 1 divide qualquer número
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                soma += d
                if d != n // d:
                    soma += n // d
        if soma == n:
            print(n, "é perfeito")


def ex21():
    numeros = []
    while True:
        texto = input("Número (ou 'fim'): ").strip().lower()
        if texto == "fim":
            break
        try:
            numeros.append(float(texto))
        except ValueError:
            print("Valor inválido, ignorado.")
    if not numeros:
        print("Nenhum número digitado.")
        return
    print(f"Quantidade: {len(numeros)} | Soma: {sum(numeros)} | Média: {sum(numeros) / len(numeros):.2f}")
    print(f"Maior: {max(numeros)} | Menor: {min(numeros)}")


def ex22():
    lista = [int(input(f"Número {i}: ")) for i in range(1, 7)]
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    print("Original:", lista)
    print("Invertida:", invertida)


def ex23():
    palavras = input("Frase: ").split()
    maior = ""
    for p in palavras:
        if len(p) > len(maior):
            maior = p
    print(f"Palavras: {len(palavras)}")
    print(f"Maior palavra: {maior}")
    print("Em ordem:", " ".join(sorted(palavras, key=str.lower)))


def ex24():
    frase = input("Frase: ")
    sem_vogais = ""
    for c in frase:
        if c.lower() not in "aeiouáéíóúâêôãõà":
            sem_vogais += c
    print(sem_vogais)


def ex25():
    numeros = [5, 9, 3, 9, 7]
    unicos = sorted(set(numeros), reverse=True)
    if len(unicos) < 2:
        print("Não existe segundo maior")
    else:
        print(f"Lista {numeros}: segundo maior = {unicos[1]}")


def ex26():
    a = [1, 4, 7]
    b = [2, 3, 8]
    i = j = 0
    resultado = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])  # o que sobrou de uma das listas
    resultado.extend(b[j:])
    print(resultado)


def ex27():
    texto = input("Texto: ").lower()
    for sinal in ".,!?":
        texto = texto.replace(sinal, "")
    contagem = {}
    for p in texto.split():
        contagem[p] = contagem.get(p, 0) + 1
    top = sorted(contagem.items(), key=lambda item: item[1], reverse=True)[:3]
    for palavra, vezes in top:
        print(f"{palavra}: {vezes}")


def sacar_notas(valor: int) -> dict:
    """Devolve {nota: quantidade} usando o menor número de notas possível."""
    if valor in (1, 3) or valor <= 0:
        raise ValueError(f"não é possível sacar R$ {valor} com as notas disponíveis")
    resultado = {}
    restante = valor
    # A nota de 5 é a única ímpar: valor ímpar precisa de exatamente uma nota de 5.
    # (Pegar "o máximo de cada nota" falharia em 11: 10 + sobra 1.)
    if restante % 2 == 1:
        resultado[5] = 1
        restante -= 5
    for nota in [100, 50, 20, 10, 2]:  # com valor par, as notas pares sempre fecham a conta
        quantidade = restante // nota
        if quantidade > 0:
            resultado[nota] = quantidade
            restante -= quantidade * nota
    return dict(sorted(resultado.items(), reverse=True))  # da maior nota para a menor


def ex28():
    for valor in [180, 8, 11, 3]:
        try:
            print(valor, "->", sacar_notas(valor))
        except ValueError as erro:
            print(valor, "->", erro)


def ex29():
    agenda = {}
    while True:
        print("\n[1] Adicionar [2] Buscar [3] Listar [4] Remover [0] Sair")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            break
        elif opcao == "1":
            nome = input("Nome: ").strip().title()
            agenda[nome] = input("Telefone: ").strip()
        elif opcao == "2":
            nome = input("Nome: ").strip().title()
            print(agenda.get(nome, "Contato não encontrado"))
        elif opcao == "3":
            for nome in sorted(agenda):
                print(f"{nome}: {agenda[nome]}")
            if not agenda:
                print("Agenda vazia")
        elif opcao == "4":
            nome = input("Nome: ").strip().title()
            try:
                del agenda[nome]
                print("Removido")
            except KeyError:
                print("Contato não encontrado")
        else:
            print("Opção inválida")


def validar_senha(senha: str) -> list:
    problemas = []
    if len(senha) < 8:
        problemas.append("ter pelo menos 8 caracteres")
    if not any(c.isupper() for c in senha):
        problemas.append("ter uma letra maiúscula")
    if not any(c.islower() for c in senha):
        problemas.append("ter uma letra minúscula")
    if not any(c.isdigit() for c in senha):
        problemas.append("ter um número")
    if all(c.isalnum() for c in senha):
        problemas.append("ter um símbolo")
    return problemas


def ex30():
    for senha in ["abc", "senhaforte", "Senha123", "Senha@123"]:
        problemas = validar_senha(senha)
        if problemas:
            print(f"{senha!r}: fraca, precisa " + ", ".join(problemas))
        else:
            print(f"{senha!r}: forte!")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or not 1 <= int(sys.argv[1]) <= 30:
        print("Uso: python aula13/solucao.py <número do exercício de 1 a 30>")
    else:
        numero = int(sys.argv[1])
        print(f"=== Solução do exercício {numero:02} ===")
        globals()[f"ex{numero:02}"]()  # chama ex01, ex02... pelo nome
