from typing import Dict, Any

Estoque = Dict[str, Dict[str, Any]]


def exibir_menu() -> str:
    """Retorna o menu exatamente no formato solicitado."""
    return (
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade\n"
        "5 - Sair"
    )


def adicionar_produto(estoque: Estoque, nome: str, quantidade: int, preco: float) -> str:
    if nome in estoque:
        return "Erro: Produto já cadastrado."
    estoque[nome] = {"quantidade": int(nova_qtd := quantidade), "preço": float(preco)}
    return f"Produto '{nome}' adicionado com sucesso!"


def listar_produtos(estoque: Estoque) -> str:
    if not estoque:
        return "Nenhum produto cadastrado."
    linhas = ["Lista de produtos:"]
    for nome, dados in sorted(estoque.items(), key=lambda item: item[0]):
        linhas.append(
            f"{nome}: Quantidade disponível - {dados['quantidade']} | Preço - R${dados['preço']:.2f}"
        )
    return "\n".join(linhas)


def remover_produto(estoque: Estoque, nome: str) -> str:
    if nome not in estoque:
        return "Erro: Produto não encontrado."
    del estoque[nome]
    return f"Produto '{nome}' removido com sucesso!"


def atualizar_quantidade(estoque: Estoque, nome: str, nova_quantidade: int) -> str:
    if nome not in estoque:
        return "Erro: Produto não encontrado."
    estoque[nome]["quantidade"] = int(nova_quantidade)
    return f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}."
