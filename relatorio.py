def relatar(conexao):
    cursor = conexao.cursor()

    sql = '''
        SELECT cliente.nome, cliente.cpf ,transporte.descricao FROM transporte
        INNER JOIN cliente ON trasnporte.idcli = cliente.rowid
        ORDER BY 1 ASC        
    '''

    cursor.execute(sql)
    listarel = cursor.fetchall()

    print("==== Relatório de transporte ====")

    for c in listarel:
        print("""
        Cliente: {}
        CPF: {}
        Produto: {}

        """.format(c[0], c[1], c[2]))
        print("------------------------------")