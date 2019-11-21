# coding: utf-8
#Importar biblioteoca
import sqlite3


# Criação da tabela cidade
def tabela_cidade(conexao):
    cursor = conexao.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS cidade (
        nome TEXT NOT NULL,
        idest INTEGER NOT NULL,
        FOREIGN KEY(idest) REFERENCES estado(rowid)
        );'''

    cursor.execute(sql)


#Inserir dados na tabela cidade
def Inserir_dados(conexao):
    nome = input("Nome da cidade: ")
    idest = int(input("Id do estado: "))

    cursor = conexao.cursor()

    sql = '''
        INSERT INTO cidade VALUES(
            '{}',
            '{}'
        );
        '''.format(nome, idest)
    cursor.execute(sql)

    #commit para salvar
    conexao.commit()


def lista(conexao):
    cursor = conexao.cursor()

    sql = '''
        SELECT rowid, * FROM cidade;
    '''

    cursor.execute(sql)
    lista = cursor.fetchall()
    print(lista)
    idest = "Paraná"
    for c in lista:
        print('''
        ID:{}
        NOME:{}
        Estado: {}
        '''.format(c[0], c[1], idest))


# SELECT cidade.rowid, cidade.nome, estado.nome FROM cidade
# INNER JOIN estado
# ON cidade.idest = estado.rowid
