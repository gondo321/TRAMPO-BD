# importaçao da biblioteca
import sqlite3
import estado
import cidade
import cliente
import transporte


conexao = sqlite3.connect("banco.sqlite3")

#Criaçao do Menu
def Menu():
    print("""
    ------Menu------
        
        1 - Alterar produto
        2 - Deletar produto
        3 - Sair
        """)


def cadastro_cliente():

    # estado.inserir_dados(conexao)
    # cidade.Inserir_dados(conexao)
    cidade.lista(conexao)
    cliente.Inserir_dados(conexao)
    transporte.Inserir_dados(conexao)

    print("Dados inseridos!!")


#Opçao para deseja efetuar cadastro
op_cadas = input("Deseja efetuar cadastro, (S/N)?: ")

if(op_cadas == 'S' or 's' or 'Sim'):
    cadastro_cliente()
else:
    print("Ja possui cadastro!! ")

#Inicio do sistema


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

                #Sair
                #elif(opcaoMenu == 3):
                #print("Voçe desejou sair do programa, Até mais")
                #reak

                #else:
                #print("Opção invalida!! TENTE NOVAMENTE ")
