import pandas as pd
import mysql.connector
from mysql.connector import Error

try:
    # Estabelece a conexão
    
    conexao = mysql.connector.connect(
        host = 'localhost', # ou o IP do servidor
        user = 'root',
        password = '',
        database = 'escola' 
    ) 

    if conexao.is_connected():
        print('Conectado com sucesso')

    # cria um cursor (objeto que permite executar comandos SQL)
    cursor = conexao.cursor()

    # Define a query de INSERT usando placeholders (%s)
    sql = 'INSERT INTO alunos (nome, cpf, data_nascimento, email, telefone, data_matricula, id_curso) VALUES (%s, %s, %s, %s, %s, %s, %s)'

    # Valores qye serão substituidos nos placeholders, na mesm aordem
    valores = ('joana','11122253344', '2005-04-21', 'joana@email.com', '21911110002', '2026-02-07', '1')

    # Executa insert no banco, substituindo os %s pelos valores em 'valores'
    # o conector trata automaticamente aspas, datas e acentos
    cursor.execute(sql, valores)

    # confirma (grava) as alterações da transação no banco
    # sem commit(), o INSERT ficaria só na memoria e seria descartado
    conexao.commit()

    # Mostra o ID (AUTO_INCREMENR) gerado na ultima inserção
    print(f'Linha inserida. ID gerado: {cursor.lastrowid}')

    # executa uma consulta
    cursor.execute('SELECT * FROM alunos LIMIT 5')

    # busca os resultados
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)



except Error as e:
    print(f'Error ao comectar: {e}')

finally:
    # fecha o cursos (se foi criado)
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception:
            pass # se já estiver fechado ou ocorrer erro, ignore

    # fecha conexão (se foi criada e ainda está conectada)
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('Conexao encerrada.')