# ==========================
# Sistema de Biblioteca
# ==========================

# Estrutura de dados
acervo = {}
emprestimos = []


# --------------------------
# Funções auxiliares (puras, sem input)
# --------------------------

def obter_dados_livro(titulo, autor, quantidade):
    """
    Retorna os dados do livro como uma única string no formato:
    "titulo autor e quantidade"
    """
    t = str(titulo).strip()
    a = str(autor).strip()
    q = obter_quantidade_livro(quantidade)
    if isinstance(q, str):
        return q  # Retorna mensagem de erro caso quantidade inválida
    return f"{t} {a} {q}"


def obter_quantidade_livro(valor):
    try:
        if isinstance(valor, str):
            valor = valor.strip()
        quantidade = int(valor)
        if quantidade < 0:
            return "Por favor, insira um número válido para a quantidade."
        return quantidade
    except (ValueError, TypeError):
        return "Por favor, insira um número válido para a quantidade."


def validar_livro_existe(acervo_dict, titulo):
    t = str(titulo).strip()
    if t in acervo_dict:
        return True
    return f"Erro: O livro '{t}' não foi encontrado."


def obter_quantidade_livro_para_emprestimo(acervo_dict, titulo, quantidade):
    """
    Valida se a quantidade solicitada de empréstimo está disponível.
    Retorna quantidade numérica se possível, ou mensagem de erro.
    """
    t = str(titulo).strip()
    q = obter_quantidade_livro(quantidade)
    if isinstance(q, str):
        return q
    existe = validar_livro_existe(acervo_dict, t)
    if existe is not True:
        return existe
    if acervo_dict[t]["quantidade"] < q:
        return f"Não há exemplares suficientes para empréstimo. Disponível: {acervo_dict[t]['quantidade']}"
    return q  # Retorna a quantidade solicitada, não True


# --------------------------
# Operações da biblioteca
# --------------------------

def adicionar_livro(acervo_dict, titulo, autor, quantidade):
    dados = obter_dados_livro(titulo, autor, quantidade)
    if isinstance(dados, str) and "Por favor" in dados:
        return dados
    t, a, q = str(titulo).strip(), str(autor).strip(), obter_quantidade_livro(quantidade)
    acervo_dict[t] = {"autor": a, "quantidade": q}
    return f"Livro '{t}' adicionado com sucesso"


def listar_livros(acervo_dict):
    if not acervo_dict:
        return "Não há livros cadastrados."
    saida = ["=== Acervo da Biblioteca ==="]
    for t, dados in acervo_dict.items():
        saida.append(f"- {t} | Autor: {dados['autor']} | Exemplares: {dados['quantidade']}")
    saida.append("============================")
    return "\n".join(saida)


def remover_livro(acervo_dict, titulo):
    t = str(titulo).strip()
    existe = validar_livro_existe(acervo_dict, t)
    if existe is not True:
        return existe
    del acervo_dict[t]
    return f"Livro '{t}' removido com sucesso!"


def atualizar_quantidade(acervo_dict, titulo, quantidade):
    t = str(titulo).strip()
    existe = validar_livro_existe(acervo_dict, t)
    if existe is not True:
        return existe
    q = obter_quantidade_livro(quantidade)
    if isinstance(q, str):
        return q
    acervo_dict[t]["quantidade"] = q
    return f"Quantidade de exemplares do livro '{t}' atualizada para {q}"


# --------------------------
# Empréstimos
# --------------------------

def registrar_emprestimo(acervo_dict, emprestimos_list, titulo, quantidade):
    """
    Registra empréstimo de 'quantidade' exemplares do livro.
    Retorna mensagem no formato esperado pelos testes.
    """
    t = str(titulo).strip()
    q = obter_quantidade_livro_para_emprestimo(acervo_dict, t, quantidade)
    if isinstance(q, str):
        return q

    acervo_dict[t]["quantidade"] -= q
    emprestimos_list.append({"titulo": t, "quantidade": q})
    return f"{q} exemplares de '{t}' emprestados com sucesso!"


def exibir_historico_emprestimos(emprestimos_list):
    if not emprestimos_list:
        return "Não há histórico de empréstimos."
    saida = ["=== Histórico de Empréstimos ==="]
    for idx, e in enumerate(emprestimos_list, start=1):
        saida.append(f"{idx}. {e['quantidade']} exemplares de '{e['titulo']}' emprestados")
    saida.append("===============================")
    return "\n".join(saida)


# --------------------------
# Menu interativo
# --------------------------

def exibir_menu():
    return (
        "\n===== Menu Biblioteca =====\n"
        "1 - Adicionar livro\n"
        "2 - Listar livros\n"
        "3 - Remover livro\n"
        "4 - Atualizar quantidade\n"
        "5 - Registrar empréstimo\n"
        "6 - Histórico de empréstimos\n"
        "7 - Sair\n"
        "===========================\n"
    )


def menu():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            quantidade = input("Quantidade: ")
            print(adicionar_livro(acervo, titulo, autor, quantidade))

        elif opcao == "2":
            print(listar_livros(acervo))

        elif opcao == "3":
            titulo = input("Título a remover: ")
            print(remover_livro(acervo, titulo))

        elif opcao == "4":
            titulo = input("Título: ")
            quantidade = input("Nova quantidade: ")
            print(atualizar_quantidade(acervo, titulo, quantidade))

        elif opcao == "5":
            titulo = input("Título: ")
            quantidade = input("Quantidade a emprestar: ")
            print(registrar_emprestimo(acervo, emprestimos, titulo, quantidade))

        elif opcao == "6":
            print(exibir_historico_emprestimos(emprestimos))

        elif opcao == "7":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# --------------------------
# Bloco principal
# --------------------------

if __name__ == "__main__":
    menu()
