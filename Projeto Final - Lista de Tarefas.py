def adicionar_tarefa(lista_de_tarefas, tarefa):
    """
    Adiciona uma nova tarefa com status 'não concluída' à lista.
    """
    nova_tarefa = {"descricao": tarefa, "concluida": False}
    lista_de_tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso! \n")
    return lista_de_tarefas


def listar_tarefas(lista_de_tarefas):
    """
    Lista todas as tarefas com seu número e status.
    """
    print('\n')
    print("-" * 50)
    print(f"{' ' * 20}Lista de Tarefas")
    print("-" * 50)
    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        status = "✓" if tarefa["concluida"] else "✗"
        print(f"{i} - [{status}] {tarefa['descricao']}")
    print("-" * 50)


def apagar_tarefa(lista_de_tarefas, indice):
    """
    Remove uma tarefa da lista com base no índice informado.
    """
    lista_de_tarefas.pop(indice - 1)
    return lista_de_tarefas


def concluir_tarefa(lista_de_tarefas, indice):
    """
    Marca a tarefa como concluída.
    """
    lista_de_tarefas[indice - 1]["concluida"] = True
    print("Tarefa marcada como concluída! \n")
    return lista_de_tarefas


def exibir_menu():
    """
    Exibe o menu principal com opções disponíveis.
    """
    print("-" * 50)
    print("Escolha uma opção:\n" \
          "1 - Inserir uma nova tarefa;\n" \
          "2 - Listar tarefas;\n" \
          "3 - Remover tarefa da lista;\n" \
          "4 - Marcar tarefa como concluída;\n" \
          "5 - Sair.")
    print("-" * 50)


# Programa principal
lista_de_tarefas = []
continuar = True

print("=" * 50)
print("Essa é a sua lista de tarefas. Seja bem-vind(x)!")
print("=" * 50)

while continuar:
    exibir_menu()
    opcao = input("O que deseja fazer? selecione: ")

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)

    elif opcao == "3":
        tarefa = input('Insira o número da tarefa que será apagada: ')
        if not tarefa.isnumeric():
            print("Resposta inválida. Digite apenas números.")
        elif int(tarefa) > len(lista_de_tarefas) or int(tarefa) <= 0:
            print("Número inválido. Verifique e tente novamente!")
        else:
            apagar_tarefa(lista_de_tarefas, int(tarefa))

    elif opcao == "4":
        tarefa = input('Digite o número da tarefa a ser marcada como concluída: ')
        if not tarefa.isnumeric():
            print("Resposta inválida. Digite apenas números.")
        elif int(tarefa) > len(lista_de_tarefas) or int(tarefa) <= 0:
            print("Número inválido. Verifique e tente novamente!")
        else:
            concluir_tarefa(lista_de_tarefas, int(tarefa))

    elif opcao == "5":
        continuar = False

    else:
        print("Escolha uma opção válida entre (1, 2, 3, 4 ou 5). Tente novamente!")

print("\nObrigado por usar a lista de tarefas! Até logo.\n")