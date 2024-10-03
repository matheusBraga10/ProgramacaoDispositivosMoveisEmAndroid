class Armario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tamanho_armario = db.Column(db.String(80), unique=True, nullable=False)
    descricao = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Armario (
                    id INTEGER PRIMARY KEY,
                    tamanho_armario TEXT NOT NULL,
                    descricao TEXT NULL
                )
            """)
            conn.commit()
            print("Tabela criada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")

        armarios = [
            ('Pequeno', '1'),
            ('Medio', '2')
        ]

        try:
            cursor.executemany("""
                INSERT INTO Armario (tamanho_armario, descricao)
                VALUES (?, ?)
            """, armarios)
            conn.commit()
            print("Dados inseridos com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()
