import sqlite3
conexao = sqlite3.connect("Atividade02.sqlite3")
cursor = conexao.cursor()
#######################################################################################

sql_organizadores = """
CREATE TABLE IF NOT EXISTS organizadores(
    id INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    cpf VARCHAR(11) UNIQUE,
    evento_id INT,
        PRIMARY KEY(id)
)
"""
cursor.execute(sql_organizadores)

sql_aventos = """
CREATE TABLE IF NOT EXISTS eventos(
    id INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    data DATE NOT NULL,
    local VARCHAR(100) NOT NULL,
        PRIMARY KEY(id)
);    
"""
cursor.execute(sql_aventos)

sql_organizadores_eventos = """
CREATE TABLE IF NOT EXISTS organizador_evento(
    organizador_id INT,
    evento_id INT,
        FOREIGN KEY (organizador_id) REFERENCES organizadores(id)
        FOREIGN KEY (evento_id) REFERENCES eventos(id)
CONSTRAINT pk_organ_event PRIMARY KEY(organizador_id,evento_id)
);
"""
cursor.execute(sql_organizadores_eventos)
#######################################################################################
conexao.commit()
conexao.close()