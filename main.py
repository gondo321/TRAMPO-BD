# coding: utf-8
# importaçao da biblioteca


import sqlite3
import tabelaEstado
import tabelaCidade
import tabelaCliente
import tabelaTransporte

from getpass import getpass

conexao = sqlite3.connect("banco.sqlite")
# tabelaEstado.tabela_estado(conexao)
# tabelaCidade.tabela_cidade(conexao)
# tabelaCliente.tabela_cliente(conexao)
# tabelaTransporte.tabela_transporte(conexao)


#tabelaEstado.inserirdados(conexao)
#tabelaCidade.Inserir_dados(conexao)


#Criaçao do Menu



# def Menu():
#      print("""
#      ------Menu------

#      1 - Alterar produto
#      2 - Deletar produto
#      3 - Relatoro: Nome e Produto
#      4 - Sair
#      """)


def cadastro_cliente():

    #tabelaCidade.Inserir_dados(conexao)
    tabelaCidade.lista(conexao)
    tabelaCliente.Inserir_dados(conexao)
    
    


#Opçao para deseja efetuar cadastro
op_cadas = input("Deseja efetuar cadastro, (S/N)?: ")
op_cadas = op_cadas.lower()
if(op_cadas == 's' ):
    cadastro_cliente()
else:
    print("Ja possui cadastro!! ")

#Inicio do sistema
#tabelaEstado.inserir_dados(conexao)
#tabelaCidade.inserir_dados(conexao)


def sistema(conexao):
    cursor = conexao.cursor()
    print("Seja bem vindo a nossa tela!!")
    print(" ")
     #Logar na conta
    CPF = input("CPF: ")
    senha = getpass("Senha: ")

    sql = '''
     SELECT rowid, * FROM cliente;
     '''
    cursor.execute(sql)

    listar_cli = cursor.fetchall()

    for c in listar_cli:
        if(CPF == c[5] and senha == c[6]):
            print(" Logado com sucesso ")
            
            
            
            while(True):
                
                print("""
     ------Menu------

     1 - Inserir produto
     2 - Alterar produto
     3 - Deletar Produto
     4 - Relatorio Nome, Produto: 
     5 - Sair
     """)
                # Opção Menu
                opcaoMenu = int(input("Digite a opção que deseje: "))


                if(opcaoMenu == 1):
                     tabelaTransporte.Inserir_dados(conexao)


                 # Alterar produto
                elif(opcaoMenu == 2):
                    tabelaTransporte.alterar_produto(conexao)

                 # Deletar produto
                elif(opcaoMenu == 3):
                    tabelaTransporte.deleteProduto(conexao)

                 # Relatorio
                elif(opcaoMenu == 4):
                    tabelaTransporte.relatorio(conexao)

                 # Sair
                elif(opcaoMenu == 5):
                    print("Voçe desejou sair do programa, Até mais")
                    break

                else:
                    print("Opção invalida!! TENTE NOVAMENTE ")

sistema(conexao)



# # Criaçao de tabela
# #tabelaEstado.tabela_estado(conexao)
# #tabelaCidade.tabela_cidade(conexao)
# # tabelaCliente.tabela_cliente(conexao)
# # tabelaTransporte.tabela_transporte(conexao)


# #tabelaEstado.inserirdados(conexao)
# #tabelaCidade.Inserir_dados(conexao)
