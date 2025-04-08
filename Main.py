from CRUD.create import inserir
from CRUD.read import lerDados
from SGBD.conexaoBanco import conectarBanco

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Inserir nova candidatura")
        print("2 - Consultar candidaturas")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            inserir()
        elif opcao == "2":
            conexao = conectarBanco()
            if conexao:
                lerDados(conexao)
                conexao.close()
            else:
                print("Erro ao conectar ao banco de dados.")
        elif opcao == "3":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
