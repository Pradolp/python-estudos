# Aula 03 - Solução (abra só depois de tentar!)

# Exercício 1
n = int(input("Número: "))
if n % 2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é ímpar")

# Exercício 2
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2  # parênteses: sem eles só a nota2 seria dividida
print(f"Média: {media:.1f}")
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Exercício 3
ano = int(input("Ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")

# Exercício 4
a = float(input("Primeiro: "))
b = float(input("Segundo: "))
c = float(input("Terceiro: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(f"O maior é {maior}")

# Exercício 5
LIMITE = 80  # maiúsculas: convenção para valores que não mudam (constantes)
velocidade = float(input("Velocidade (km/h): "))
if velocidade > LIMITE:
    multa = (velocidade - LIMITE) * 7
    print(f"Multado! Valor: R$ {multa:.2f}")
else:
    print("Dentro do limite. Boa viagem!")
