# Contexto do projeto

Repositório de estudos de Python do Lucas Prado (GitHub: Pradolp/python-estudos).
Iniciante em programação, seguindo o roadmap "Do zero à primeira vaga em IA"
(artifact no claude.ai: https://claude.ai/artifact/68EWvQYWaYcN5pwjHVCQ2s).

## O que é este repositório

Curso que cobre a fase 0 do roadmap, **"Python do zero"**, em 14 aulas (`aula01` a
`aula14`). Cada aula tem `README.md` (teoria), `exemplos.py`, `exercicio.py` e
`solucao.py`. Exceções: a aula 10 tem o pacote `ferramentas/` e
`solucao_conversoes.py`; a aula 13 tem `exercicios.md` (os 30 exercícios), `modelo.py`
e `solucao.py <n>`; a aula 14 tem `jogo.py` (esqueleto) no lugar de `exercicio.py`.
O índice das aulas está no `README.md` da raiz.

As próximas fases do roadmap são: Git/GitHub e terminal; depois Web, APIs e SQL
(requests, ViaCEP, SQLite, FastAPI, pytest); depois LLMs com LangChain 1.x
(`init_chat_model`, `create_agent`).

## Como trabalhar comigo

- Escreva tudo em **português do Brasil**, com linguagem simples para iniciante.
- Use o estilo de ensino: explique o porquê, dê insights curtos e deixe o Lucas escrever
  as partes que valem como aprendizado. Não resolva exercícios por ele, a menos que ele peça.
- **Git: faça um commit para cada arquivo criado ou modificado**, com mensagem em
  português ("Adiciona...", "Corrige..."). Quem faz o `git push` é o Lucas, com a
  chave SSH dele.
- Antes de dar algo como pronto, rode os arquivos `.py` para conferir.

## Ambiente

- Começou no Windows 11 (PowerShell, Python 3.13). Em 2026-10 ele foi migrar para **Ubuntu**.
  No Ubuntu, use `python3` e `source .venv/bin/activate`. Os comandos da aula 11 estão
  escritos para Windows: adapte quando for explicar.
- Editor: VS Code com as extensões Python e Jupyter. Ele usa células `# %%`
  (Interactive Window, precisa do `ipykernel`) para rodar só um trecho do código.
  Lembrete: a célula vai do `# %%` até o próximo `# %%`.

## Onde ele parou (atualize esta seção)

- O curso das 14 aulas está pronto. O Lucas está começando a aula 01: o exercício 1 de
  `aula01/exercicio.py` tem um `TODO(human)` para ele.
- Ele estava testando células `# %%` em `aula01/exemplos.py`.
