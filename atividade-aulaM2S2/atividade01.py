from funcoes import *
import sqlite3
conexao = sqlite3.connect("Banco.sqlite3")
cursor = conexao.cursor()
#######################################################################################

sql = """
CREATE TABLE categoria(
    id INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    status INT CHECK(status IN (0,1)),
    categoria_id INT,
        PRIMARY KEY(id)
        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);    
"""