# Aula 04 - Solução (abra só depois de tentar!)

# Exercício 1
quantidade = 0
soma = 0
numero = float(input("Número (0 para parar): "))
while numero != 0:
    quantidade += 1
    soma += numero
    numero = float(input("Número (0 para parar): "))
if quantidade > 0:
    print(f"{quantidade} números | soma {soma} | média {soma / quantidade:.2f}")
else:
    print("Nenhum número digitado.")

# Exercício 2
SENHA = "python123"
tentativas = 0
acertou = False
while tentativas < 3 and not acertou:
    tentativa = input("Senha: ")
    tentativas += 1
    if tentativa == SENHA:
        acertou = True
    else:
        print(f"Senha errada. Restam {3 - tentativas} tentativas.")
if acertou:
    print("Acesso liberado")
else:
    print("Conta bloqueada")

# Exercício 3
sexo = input("Sexo [M/F]: ").strip().upper()
while sexo not in ("M", "F"):
    print("Valor inválido")
    sexo = input("Sexo [M/F]: ").strip().upper()
print("Registrado:", sexo)

# Exercício 4
termos = int(input("Quantos termos? "))
anterior, atual = 0, 1
contador = 0
while contador < termos:
    print(anterior, end=" ")
    anterior, atual = atual, anterior + atual  # troca simultânea
    contador += 1
print()

# Exercício 5
numero = float(input("Número (negativo para parar): "))
if numero < 0:
    print("Nenhum número válido.")
else:
    maior = menor = numero  # o primeiro número é o maior e o menor até agora
    while numero >= 0:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        numero = float(input("Número (negativo para parar): "))
    print(f"Maior: {maior} | Menor: {menor}")
