import sqlite3
conexao = sqlite3.connect("Atividade01.sqlite3")
cursor = conexao.cursor()
#######################################################################################

sql_categorias = """
CREATE TABLE IF NOT EXISTS categorias(
    id INT NOT NULL,
    categoria VARCHAR(50) NOT NULL,
        PRIMARY KEY(id)
)
"""
cursor.execute(sql_categorias)

sql_tarefas = """
CREATE TABLE IF NOT EXISTS tarefas(
    id INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    categoria_id INT,
    status INT CHECK(status IN (0,1)),
        PRIMARY KEY(id),
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);    
"""
cursor.execute(sql_tarefas)
#######################################################################################
conexao.commit()
conexao.close()