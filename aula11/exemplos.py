# Aula 11 - Exemplos: ambiente virtual e pip
# Rode duas vezes para comparar:
#   1) sem ambiente:     python aula11/exemplos.py
#   2) com ambiente:     (siga o README para criar e ativar o .venv e instalar o requests)
#                        python exemplos.py

import sys
from importlib import metadata

print("=== Qual Python está rodando? ===")
print("Executável:", sys.executable)
print("Versão:", sys.version.split()[0])

em_venv = sys.prefix != sys.base_prefix
if em_venv:
    print("Ambiente virtual ATIVO em:", sys.prefix)
else:
    print("Você está no Python do sistema (nenhum ambiente virtual ativo).")

print("\n=== Pacotes instalados neste Python ===")
pacotes = sorted(f"{d.metadata['Name']}=={d.version}" for d in metadata.distributions())
if pacotes:
    for p in pacotes[:15]:
        print(" ", p)
    if len(pacotes) > 15:
        print(f"  ... e mais {len(pacotes) - 15}")
else:
    print("  (nenhum)")

print("\n=== Usando um pacote de terceiros: requests ===")
try:
    import requests
except ModuleNotFoundError:
    print("O pacote 'requests' não está instalado neste Python.")
    print("Ative o .venv e rode: pip install requests")
else:
    print("requests versão", requests.__version__)
    print("Consultando a API do ViaCEP (cep 01001-000)...")
    try:
        resposta = requests.get("https://viacep.com.br/ws/01001000/json/", timeout=10)
        dados = resposta.json()  # o JSON vira um dicionário Python
        print(f"  {dados['logradouro']} - {dados['bairro']}, {dados['localidade']}/{dados['uf']}")
    except requests.RequestException as erro:
        print("  Sem conexão com a internet?", erro)
