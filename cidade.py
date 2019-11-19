#Importar biblioteoca
import sqlite3


# Criação da tabela cidade
def tabela_cidade(conexao):
    cursor = conexao.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS cidade,
        nome TEXT NOT NULL,
        idest INTEGER NOT NULL,
        FOREIGN KEY(idest) REFERENCES estado(rowid)
        );'''

    cursor.execute(sql)


#Inserir dados na tabela cidade
def Inserir_dados(conexao):
    nome = input("Nome da cidade: ")
    idest = gvcjh

    cursor = conexao.cursor()

    sql = '''
        INSERT INTO cidade VALUES(
            '{}'
        );
        '''.format(nome)
    cursor.execute(sql)

    #commit para salvar
    conexao.commit()


def lista(conexao):
    cursor = conexao.cursor()

    sql = '''
        SELECT rowid, * FROM cidade;
    '''

    cursor.execute(sql)
    lista_cidade = cursor.fetchall()
    for c in lista_cidade:
        print('''
        ID:{}
        NOME:{}
        idest: {}

        ''').format(c[0],c[1],c[2])

