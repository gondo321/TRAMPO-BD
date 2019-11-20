# coding: utf-8
# importar biblioteca
import sqlite3
import tabelaCliente
#Criação da tabela


def tabela_transporte(conexao):
    cursor = conexao.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS transporte(
        descricao TEXT NOT NULL,
        cidOrig INTEGER NOT NULL,
        cidDest INTEGER NOT NULL,
        idcli INTEGER NOT NULL,
        FOREIGN KEY(cidOrig) REFERENCES cidade(rowid),
        FOREIGN KEY(cidDest) REFERENCES cidade(rowid),
        FOREIGN KEY(idcli) REFERENCES cliente(rowid)
    ); '''

    cursor.execute(sql)


#Inserir dados
def Inserir_dados(conexao):
    cid_Orig = input("Digite a cidade Origem: ")
    cid_dest = input("Digite sua cidade de destino:  ")
    descricao = input("Digite a descrição do produto: ")
    idcli = tabelaCliente.listar_cliente(conexao)

    cursor = conexao.cursor()

    sql = '''
        INSERT INTO transporte VALUES(
            '{}',
            '{}',
            '{}',
            '{}'
        );
        '''.format(descricao, cid_Orig, cid_dest, idcli)

    cursor.execute(sql)

    #Commit para salvar
    conexao.commit()

#Alterar produto


def alterar_produto(conexao):

    cursor = conexao.cursor()

    sql = """ SELECT rowid, * transporte;   
    """
    cursor.execute(sql)
    listatrans = cursor.fetchall()

    # Listando transporte
    print("==== Lista de transportes ====")
    
    for t in listatrans:
        print("""
        Produto: {}
        Cidade origem: {}
        Cidade destino: {}
        ID Cliente: {}       
        """.format(t[1], t[2], t[3], t[4]))
        

    id = int(input("Digite o ID do transporte a ser alterado: "))

    for i in listatrans:
        if (id == i[0]):
            print(" ")
            a = input("Nova descrição: ")
            
            # Atualização da descrição
            sql = """ UPDATE transporte SET descricao = {} WHERE rowid = {}
            """.format(a, id)
            cursor.execute(sql)
            conexao.commit()
            print(" ")
            print("Atualização efetuada!")


def deleteProduto(conexao):
    cursor = conexao.cursor()
    id = int(input("Insira o ID para excluir: "))

    sql = '''
        SELECT rowid, * FROM transporte;
    '''

    cursor.execute(sql)

    #Confirmação para deletar
    delete = input("Deseja mesmo Deletar o produto: ")

    if(delete == 'Sim' or delete == 's' or delete == 'S'):
        sql_excluir = '''
            DELETE rowid, * FROM transporte
            WHERE rowid = {}
    '''.format(id)
    cursor.execute(sql_excluir)
    conexao.commit()

    print("Deletado com sucesso!")

def relatorio(conexao):
    cursor = conexao.cursor()

    sql = '''
        SELECT cliente.nome "Nome do cliente" , transporte.descricao "Produto"
        FROM transporte INNER JOIN descricao ON transporte.idtrans = cliente.idtrans
    '''

    cursor.execute(sql)

    lista_relatorio = cursor.fetchall()

    print("==== Relatórios ====")
    for r in lista_relatorio:
        print("""
        Cliente: {}
        Produto: {}
        """.format(r[0], r[1]))