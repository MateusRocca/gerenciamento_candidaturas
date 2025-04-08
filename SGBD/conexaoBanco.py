from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def conectarBanco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SenhaPadrao9%",
            database="vagas"
        )

        if conexao.is_connected():
            print('Conectado ao banco de dados')
        return conexao

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

conexao = conectarBanco()
if conexao:
    conexao.close()