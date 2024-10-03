class Tabela_de_Entregas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    morador_id = db.Column(db.Integer, unique=True, nullable=False, foreign_key=True)
    data_entrega = db.Column(db.DateTime, unique=True, nullable=False)
    data_retirada = db.Column(db.DateTime, unique=True, nullable=False)
    codigo_gerado = db.Column(db.Integer, unique=True, nullable=False)
    status = db.Column(db.String(80), unique=True, nullable=False)
    armario_id = db.Column(db.Integer, unique=True, nullable=False, foreign_key=True)

    def __init__(self):
        self.criar_tabela_entregas()


# Função para criar a tabela de entregas
def criar_tabela_entregas():
    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tabela_de_Entregas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                morador_id INTEGER NULL,
                data_entrega DATETIME NULL,
                data_retirada DATETIME NULL,
                codigo_gerado TEXT NULL,
                status TEXT NULL,
                armario_id INTEGER NULL,
                FOREIGN KEY (morador_id) REFERENCES Cadastro(id),
                FOREIGN KEY (armario_id) REFERENCES Armario(id)
            )
        """)
        conn.commit()
        print("Tabela de entregas criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela de entregas: {e}")
    finally:
        conn.close()

# Função para buscar as entregas no banco de dados
def buscar_entregas():
    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT e.id, m.nome, e.data_entrega, e.data_retirada, a.descricao, e.status, a.status
            FROM Tabela_de_Entregas e
            JOIN Cadastro m ON e.morador_id = m.id
            LEFT JOIN Armario a ON e.armario_id = a.id
        """)
        entregas = cursor.fetchall()
        return entregas
    except sqlite3.Error as e:
        print(f"Erro ao buscar entregas: {e}")
        return []
    finally:
        conn.close()


