from SGBD.ConexaoBanco import conectarBanco

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