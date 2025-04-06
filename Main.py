from Insert.InserirDados import inserirDados

nome_vaga = input('Insira o nome da vaga: ')
nome_empresa = input('Insira o nome da Empresa: ')
descricao_vaga = input('Insira a descrição da vaga: ')
salario = input('Insira o salário: ')
candidatura_status = input('Insira o status da candidatura(Em andamento, Encerrada: ')

# Debug
print("\nDADOS A ENVIAR:")
print("Nome vaga:", nome_vaga)
print("Empresa:", nome_empresa)
print("Descrição:", descricao_vaga)
print("Salário:", salario)
print("Status:", candidatura_status)
print("\n")

inserirDados(nome_vaga, nome_empresa, descricao_vaga, salario, candidatura_status)