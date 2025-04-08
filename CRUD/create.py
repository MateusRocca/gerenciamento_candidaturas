from SGBD.conexaoBanco import conectarBanco

def inserirDados(nome_vaga, nome_empresa, descricao_vaga, salario, candidatura_status):
    conexao = conectarBanco()
    if not conexao:
        print("Não foi possível conectar ao banco.")
        return
    cursor = conexao.cursor()

    sql = """
        INSERT INTO candidaturas (nome_vaga, nome_empresa, descricao_vaga, salario, candidatura_status) VALUES (%s, %s, %s, %s, %s)
    """
    valores = (nome_vaga, nome_empresa, descricao_vaga, salario, candidatura_status)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Dados inseridos com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

    finally:
        cursor.close()
        conexao.close()

def inserir():
    print("\n---- INSERIR NOVA CANDIDATURA ----")
    nome_vaga = input('Insira o nome da vaga: ').strip()
    nome_empresa = input('Insira o nome da Empresa: ').strip()
    descricao_vaga = input('Insira a descrição da vaga: ').strip()
    salario = input('Insira o salário: ').strip()
    candidatura_status = input('Insira o status da candidatura (Em andamento, Encerrada): ').strip()

    inserirDados(nome_vaga, nome_empresa, descricao_vaga, salario, candidatura_status)
