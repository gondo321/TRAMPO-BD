# importaçao da biblioteca
import sqlite3
import tabelaEstado
import tabelaCidade
import tabelaCliente
import tabelaTransporte


conexao = sqlite3.connect("banco.sqlite3")

#Criaçao do Menu
def Menu():
    print("""
    ------Menu------
        
    1 - Alterar produto
    2 - Deletar produto
    3 - Relatoro: Nome e Produto 
    4 - Sair
    """)


def cadastro_cliente():

    #estado.inserir_dados(conexao)
    #cidade.Inserir_dados(conexao)
    tabelaCidade.lista(conexao)
    tabelaCliente.Inserir_dados(conexao)
    tabelaTransporte.Inserir_dados(conexao)

    print("Dados inseridos!!")


#Opçao para deseja efetuar cadastro
op_cadas = input("Deseja efetuar cadastro, (S/N)?: ")

if(op_cadas == 'S' or 's' or 'Sim'):
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
    senha = int(input("Senha: "))

    sql = '''
    SELECT rowid, * FROM cliente;
    '''
    cursor.execute(sql)

    listar_cli = cursor.fetchall

    for c in listar_cli:
        if(CPF == c[5] and senha == c[6]):
            print(" Logado com sucesso ")
            while(True):
                Menu()
                #Opção Menu
                #opcaoMenu = int(input("Digite a opção que deseje: "))

                #Alterar produto
                #if(opcaoMenu == 1):

                #Deletar produto
                #if(opcaoMenu == 2):

                #Relatorio
                #elif(opcaoMenu == 3):



                #Sair
                #elif(opcaoMenu == 4):
                #print("Voçe desejou sair do programa, Até mais")
                #reak

                #else:
                #print("Opção invalida!! TENTE NOVAMENTE ")







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Opção Menu
        #opcaoMenu = int(input("Digite a opção que deseje: "))


    #Criaçao do cadastro do cliente
   
        #if(opcaoMenu == 1):
           #tabelaEstado.inserir_dados(conexao)
            #tabelaCidade.Inserir_dados(conexao)
            #tabelaCliente.Inserir_dados(conexao)
            #tabelaTransporte.Inserir_dados(conexao)

        #Logar
        #while(True):    
        #elif(opcaoMenu == 2):
            #tabelaCliente.logar_conta(conexao)


        #Alterar produto
        #elif(opcaoMenu == 3):


        #Deletar produto 
        #elif(opcaoMenu == 4):

        
        #Sair
        #elif(opcaoMenu == 5):
            #print("Voçe desejou sair do programa, Até mais")
            #break
        
        #else:
           #print("Opção invalida!! TENTE NOVAMENTE ")
        






















#Chamando o procedimento da tabela estado
#tabelaEstado.tabela_estado
#tabelaEstado.inserir_dados

#Chamando o procedimento da tabela cidade
#tabelaCidade.tabela_cidade
#tabelaCidade.Inserir_dados

#Chamando o procedimento  da tabela cliente
#tabelaCliente.tabela_cliente
#tabelaCliente.Inserir_dados

#Chamando o procedimento da tabela transporte
#tabelaTransporte.tabela_transporte
#tabelaTransporte.Inserir_dados