lista = []


# Função para exibir o menu
def exibir_menu():
    print("\n===== LISTA DE COMPRAS =====")
    print("1 - Adicionar Produto")
    print("2 - Visualizar Lista")
    print("3 - Remover Produto")
    print("4 - Sair")


while True:
    exibir_menu()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome_produto = input("Informe o nome do produto: ")
        lista.append(nome_produto)
        print(f"{nome_produto} foi adicionado à lista.")

    elif opcao == 2:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            print("\nProdutos na lista:")
            for produto in lista:
                print(f"- {produto}")

    elif opcao == 3:
        produto_remover = input("Informe o produto que deseja remover: ")

        if produto_remover in lista:
            lista.remove(produto_remover)
            print(f"{produto_remover} foi removido da lista.")
        else:
            print("Produto não encontrado na lista.")

    elif opcao == 4:
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")