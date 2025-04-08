from SGBD.conexaoBanco import conectarBanco

def exibir_candidatura(candidatura):
    print("\n--- Candidatura ---")
    print(f"ID: {candidatura['id']}")
    print(f"Nome da vaga: {candidatura['nome_vaga']}")
    print(f"Empresa: {candidatura['nome_empresa']}")
    print(f"Status: {candidatura['candidatura_status']}")


def exibirTodas(cursor):
    cursor.execute("SELECT * FROM candidaturas LIMIT 100")
    candidaturas = cursor.fetchall()
    print(f"Total de candidaturas encontradas: {len(candidaturas)}")
    if candidaturas:
        print("\n---- CANDIDATURAS ----")
        for candidatura in candidaturas:
            exibir_candidatura(candidatura)
    else:
            print("Nenhuma candidatura encontrada.")


def exibirPorID(cursor):
    id = input("Digite o ID da candidatura: ")
    cursor.execute("SELECT * FROM candidaturas WHERE id = %s", (id,))
    candidatura = cursor.fetchone()
    if candidatura:
        exibir_candidatura(candidatura)
    else:
        print("Candidatura não encontrada.")

def exibirPorEmpresa(cursor):
    empresa = input("Digite o nome da empresa: ")
    cursor.execute("SELECT * FROM candidaturas WHERE nome_empresa LIKE %s", (f"%{empresa}%",))
    candidaturas = cursor.fetchall()
    if candidaturas:
        print("\n---- CANDIDATURAS ----")
        for candidatura in candidaturas:
            exibir_candidatura(candidatura)
    else:
        print("Nenhuma candidatura encontrada.")

def exibirPorVaga(cursor):
    vaga = input("Digite o nome da vaga: ")
    cursor.execute("SELECT * FROM candidaturas WHERE nome_vaga LIKE %s", (f"%{vaga}%",))
    candidaturas = cursor.fetchall()
    if candidaturas:
        print("\n---- CANDIDATURAS ----")
        for candidatura in candidaturas:
            exibir_candidatura(candidatura)
    else:
        print("Nenhuma candidatura encontrada.")

def exibirPorStatus(cursor):
    status = input("Digite o status da candidatura: ")
    cursor.execute("SELECT * FROM candidaturas WHERE candidatura_status LIKE %s", (f"%{status}%",))
    candidaturas = cursor.fetchall()
    if candidaturas:
        print("\n---- CANDIDATURAS ----")
        for candidatura in candidaturas:
            exibir_candidatura(candidatura)
    else:
        print("Nenhuma candidatura encontrada.")

def exibir_candidatura(candidatura):
    print("\n--- Candidatura ---")
    print(f"ID: {candidatura['id']}")
    print(f"Nome da vaga: {candidatura['nome_vaga']}")
    print(f"Empresa: {candidatura['nome_empresa']}")
    print(f"Status: {candidatura['candidatura_status']}")

def lerDados(conexao):
    cursor = conexao.cursor(dictionary=True)

    try:
        while True:
            print("\n ---- MENU DE CONSULTA ----")
            print("1 - Listar todas as candidaturas")
            print("2 - Listar candidaturas por ID")
            print("3 - Listar candidaturas por empresa")
            print("4 - Listar candidaturas por vaga")
            print("5 - Listar candidaturas por status")
            print("6 - Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                exibirTodas(cursor)
            elif opcao == "2":
                exibirPorID(cursor)
            elif opcao == "3":
                exibirPorEmpresa(cursor)
            elif opcao == "4":
                exibirPorVaga(cursor)
            elif opcao == "5":
                exibirPorStatus(cursor)
            elif opcao == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar dados: {e}")


if __name__ == "__main__":
    from SGBD.conexaoBanco import conectarBanco
    conexao = conectarBanco()
    if conexao:
        lerDados(conexao)
    else:
        print("Não foi possível conectar ao banco de dados.")
