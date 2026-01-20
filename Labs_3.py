tarefas = {}



def adicionar_tarefa(tarefas):
    nome = input("Insira o nome do tarefa: ").strip()
    if nome in tarefas:
        print("Essa tarefa já existe.")
        return tarefas
    else:
        tarefas[nome] = False
        print(f"Tarefa '{nome}' adicionada com sucesso.")
        return tarefas


def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada!"
    else:
        resultado = []
        for nome, concluida in sorted(tarefas.items(), key=lambda item: item[0]):
            status = "✅ Concluída!" if concluida else "❌ Não concluída!"
            resultado.append(f"{nome}: {status}")
        return "\n".join(resultado)


def remover_tarefa(tarefas):
    nome = input("Insira o nome da tarefa: ").strip()
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."

def marcar_concluida(tarefas):
    nome = input("Insira o nome da tarefa: ").strip()
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."


def exibir_menu():
    return (
        "1 - Adicionar tarefa",
        "2 - Listar tarefa",
        "3 - Remover tarefa",
        "4 - Marcar concluida",
        "5 - Sair",
    )


def main():
    tarefas = {}
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opçao: ").strip()
        if opcao == 1:
            print(adicionar_tarefa(tarefas))
        elif opcao == 2:
            print(listar_tarefas(tarefas))
        elif opcao == 3:
            print(remover_tarefa(tarefas))
        elif opcao == 4:
            print(marcar_concluida(tarefas))
        elif opcao == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")
if __name__ == "__main__":
    main()