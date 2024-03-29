# coding: utf-8
#Importar biblioteca
import sqlite3
from getpass import getpass


#Criação da tabela
def tabela_cliente(conexao):
    cursor = conexao.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS cliente(
        nome TEXT NOT NULL,
        data_nasc TEXT NOT NULL,
        bairro TEXT NOT NULL,
        rua TEXT NOT NULL,
        cpf TEXT(11) NOT NULL,
        senha TEXT NOT NULL,
        idcid INTEGER NOT NULL,
        FOREIGN KEY(idcid) REFERENCES cidade(rowid)
    
    );'''

    cursor.execute(sql)


#Inserir dados
def Inserir_dados(conexao):
    nome = input("Digite seu nome inteiro: ")
    data_nasc = input("Insira sua data de nascimento; XX/XX/XXXX: ")
    bairro = input("Insira o bairro: ")
    rua = input("Insira a rua: ")
    cpf = input("Insira seu cpf: ")
    senha = input("Insira sua senha:  ")

    idcid = int(input("Digite o ID da cidade: "))

    cursor = conexao.cursor()

    sql = '''
        INSERT INTO cliente VALUES(
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}'
           
        );
    '''.format(nome, data_nasc, bairro, rua, cpf, senha, idcid)

    cursor.execute(sql)

    #commit para salvar
    conexao.commit()


print("Dados Inseridos!!")


#Listar o cliente
def listar_cliente(conexao):
    cursor = conexao.cursor()

    sql = '''
        SELECT rowid, * FROM cliente
        '''

    cursor.execute(sql)

    listarCliente = cursor.fetchall()

    #Listando o cliente
    for i in listarCliente:
        print('''
        ID: {}
        NOME: {}
        DATA DE NASCIMENTO: {}
        BAIRRO: {}
        rua : {}
        CPF: {}
        SENHA: {}
    '''.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    x = int(input("Digite seu ID de cliente: "))
    return x
