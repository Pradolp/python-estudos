# Aula 11 - Solução (abra só depois de tentar!)
# Precisa do requests instalado no ambiente ativo.
import requests

URL = "https://viacep.com.br/ws/{cep}/json/"


def buscar_cep(cep: str) -> dict:
    """Consulta o ViaCEP. Lança ValueError se o CEP for inválido ou não existir."""
    cep = cep.replace("-", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        raise ValueError("o CEP deve ter 8 dígitos")
    resposta = requests.get(URL.format(cep=cep), timeout=10)
    dados = resposta.json()
    if "erro" in dados:
        raise ValueError("CEP não encontrado")
    return dados


while True:
    entrada = input("\nCEP (ou 'sair'): ")
    if entrada.lower() == "sair":
        break
    try:
        endereco = buscar_cep(entrada)
    except ValueError as erro:
        print("Erro:", erro)
    except requests.RequestException:
        print("Não foi possível acessar o ViaCEP. Verifique sua internet.")
    else:
        print(f"Rua:    {endereco['logradouro'] or '(não informada)'}")
        print(f"Bairro: {endereco['bairro'] or '(não informado)'}")
        print(f"Cidade: {endereco['localidade']}/{endereco['uf']}")
