# coding: utf-8
# Biblioteca sqlite3
import sqlite3

#Criar tabela estado


def tabela_estado(conexao):
    cursor = conexao.cursor()

    sql = ''' 
        CREATE TABLE IF NOT EXISTS estado (
        nome TEXT NOT NULL,
        sigla TEXT(2) NOT NULL
        );'''

    cursor.execute(sql)

#Inserir dados da tabela estado


def inserirdados(conexao):

    nome_estado = input("Digite o estado: ")
    sigla_estado = input("Digite a sigla: ")

    cursor = conexao.cursor()

    sql = '''
        INSERT INTO estado VALUES(
            '{}',
            '{}'
        );
    ''' .format(nome_estado, sigla_estado)

    cursor.execute(sql)

    #commit para salvar
    conexao.commit()
