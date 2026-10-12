# Aula 11: ambiente virtual (`venv`) e `pip`

## 1. O problema

Cada projeto precisa de bibliotecas diferentes, e às vezes de **versões**
diferentes da mesma biblioteca. O Projeto 1 do roadmap pode precisar do
`langchain` 1.0 enquanto um projeto antigo usa outra versão. Se tudo for instalado
"no Python do computador", um projeto quebra o outro.

**Solução:** cada projeto tem o seu **ambiente virtual**, uma pasta (`.venv`) com
uma cópia isolada do Python e das bibliotecas daquele projeto.

## 2. `pip`: o instalador de pacotes

O `pip` baixa pacotes do **PyPI** (<https://pypi.org>), o repositório oficial com
centenas de milhares de bibliotecas.

| Comando                              | O que faz                                    |
|--------------------------------------|----------------------------------------------|
| `pip install requests`               | instala um pacote                            |
| `pip install requests==2.32.3`       | instala uma versão exata                     |
| `pip install -U requests`            | atualiza (`-U` = `--upgrade`)                |
| `pip uninstall requests`             | remove                                       |
| `pip list`                           | lista o que está instalado                   |
| `pip show requests`                  | detalhes de um pacote                        |
| `pip freeze > requirements.txt`      | salva a lista de pacotes e versões num arquivo |
| `pip install -r requirements.txt`    | instala tudo o que está no arquivo           |

## 3. Passo a passo no Windows (PowerShell, terminal do VS Code)

Faça isto **dentro da pasta do projeto**. Para treinar, use a pasta `aula11`.

```powershell
cd aula11

# 1. Criar o ambiente (só uma vez por projeto)
python -m venv .venv

# 2. Ativar (toda vez que abrir um terminal novo)
.venv\Scripts\Activate.ps1
```

Se der erro dizendo que **a execução de scripts foi desabilitada**, rode uma vez
(liberando scripts só para o seu usuário) e tente ativar de novo:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Com o ambiente ativo, o terminal mostra `(.venv)` no começo da linha:

```
(.venv) PS C:\Users\...\python\aula11>
```

```powershell
# 3. Instalar pacotes (vão para dentro do .venv)
pip install requests

# 4. Guardar a lista de dependências
pip freeze > requirements.txt

# 5. Rodar seu programa
python exemplos.py

# 6. Desativar quando terminar
deactivate
```

No **Git Bash**, **Linux** ou **macOS**, a ativação é diferente:
`source .venv/bin/activate` (no Git Bash do Windows: `source .venv/Scripts/activate`).

## 4. O VS Code e o ambiente virtual

1. `Ctrl + Shift + P` e digite **Python: Select Interpreter**.
2. Escolha o que mostra `.venv`.

Daí em diante o botão ▶ e os terminais novos usam o ambiente certo, e o VS Code para
de sublinhar `import requests` como erro.

## 5. Regras de ouro

- **Um `.venv` por projeto**, criado na pasta raiz do projeto.
- **O `.venv` nunca vai para o GitHub.** Ele é pesado e específico do seu
  computador. O `.gitignore` deste repositório já ignora essa pasta.
- O que vai para o GitHub é o **`requirements.txt`**. Quem baixar o projeto recria o
  ambiente com `python -m venv .venv` + `pip install -r requirements.txt`.
- Se o ambiente estragar, apague a pasta `.venv` e crie de novo. Nada se perde.
- Use `python -m pip install ...` se ficar em dúvida sobre qual `pip` está sendo
  usado. Esse formato garante o pip do Python ativo.

## 6. Como saber se estou no ambiente virtual?

```python
import sys
print(sys.prefix)   # termina em .venv quando o ambiente está ativo
```

O `exemplos.py` desta aula faz essa verificação.

## 7. Por que isso importa para o roadmap

Na fase 4 você vai rodar:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -U langchain langchain-google-genai python-dotenv
```

Agora você sabe o que cada linha faz.

## Resumo

- `python -m venv .venv` cria; `.venv\Scripts\Activate.ps1` ativa; `deactivate` sai.
- `pip install pacote` instala no ambiente ativo.
- `pip freeze > requirements.txt` registra as dependências; `pip install -r` reinstala.
- `.venv` fica fora do Git e `requirements.txt` vai para o Git.
