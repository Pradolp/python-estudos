"""Funções para trabalhar com textos."""

import unicodedata  # módulo da biblioteca padrão para lidar com acentos


def remover_acentos(texto: str) -> str:
    """Troca letras acentuadas pela versão sem acento: 'ação' -> 'acao'."""
    decomposto = unicodedata.normalize("NFD", texto)  # separa 'ã' em 'a' + '~'
    return "".join(c for c in decomposto if unicodedata.category(c) != "Mn")


def contar_palavras(texto: str) -> int:
    """Quantidade de palavras separadas por espaço."""
    return len(texto.split())


def criar_slug(texto: str) -> str:
    """Transforma um título em texto para URL: 'Olá Mundo!' -> 'ola-mundo'."""
    texto = remover_acentos(texto.lower())
    so_letras = "".join(c if c.isalnum() else " " for c in texto)
    return "-".join(so_letras.split())
