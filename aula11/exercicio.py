# Aula 11 - Exercício: seu primeiro projeto com ambiente virtual
#
# Parte 1: no terminal (siga o README desta aula)
#   [ ] Entrar na pasta aula11:                cd aula11
#   [ ] Criar o ambiente:                      python -m venv .venv
#   [ ] Ativar:                                .venv\Scripts\Activate.ps1
#   [ ] Conferir que aparece (.venv) no terminal
#   [ ] Instalar o requests:                   pip install requests
#   [ ] Gerar o arquivo de dependências:       pip freeze > requirements.txt
#   [ ] Abrir o requirements.txt e ver o que tem dentro
#   [ ] No VS Code: Python: Select Interpreter -> escolher o .venv
#   [ ] Rodar o exemplos.py e ver a mensagem "Ambiente virtual ATIVO"
#
# Parte 2: o programa (escreva abaixo e rode com: python exercicio.py)
#   Faça um consultor de CEP usando o requests e a API gratuita do ViaCEP:
#     URL: https://viacep.com.br/ws/{cep}/json/
#   Requisitos:
#   - Pedir o CEP em loop até o usuário digitar "sair"
#   - Aceitar CEP com ou sem traço (limpe com .replace("-", ""))
#   - Validar que tem 8 dígitos (dica: .isdigit() e len())
#   - Se o CEP não existir, a API devolve {"erro": "true"}: avise o usuário
#   - Tratar falta de internet com try/except requests.RequestException
#   - Mostrar: rua, bairro, cidade e estado
#
# Parte 3: teste de recriação
#   [ ] deactivate e apague a pasta .venv
#   [ ] Recrie: python -m venv .venv, ative, pip install -r requirements.txt
#   [ ] Rode de novo. Funcionou? É assim que outra pessoa vai rodar seu projeto.

# Escreva seu código aqui:

