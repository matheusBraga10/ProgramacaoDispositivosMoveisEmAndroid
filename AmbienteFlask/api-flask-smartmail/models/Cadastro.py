class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    sobrenome = db.Column(db.String(80), unique=True, nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.Integer, unique=True, nullable=False)
    cep = db.Column(db.Integer, unique=True, nullable=False)
    rua = db.Column(db.String(80), unique=True, nullable=False)
    n_ap = db.Column(db.Integer, unique=True, nullable=False)
    bairro = db.Column(db.String(80), unique=True, nullable=False)
    numero = db.Column(db.String(80), unique=True, nullable=False)
    cidade = db.Column(db.String(80), unique=True, nullable=False)
    estado = db.Column(db.String(80), unique=True, nullable=False)
    senha1 = db.Column(db.String(120), nullable=False)
    def __init__(self):
        self.criar_tabela()

    def criar_tabela():
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Cadastro (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    sobrenome TEXT NOT NULL,
                    cpf INTEGER NULL, 
                    email TEXT NOT NULL,
                    telefone INTEGER NULL,
                    cep INTEGER NULL,
                    rua TEXT NULL,
                    N_ap INTEGER NULL,
                    bairro TEXT NULL,
                    numero TEXT NULL,
                    cidade TEXT NULL,
                    estado TEXT NULL,
                    senha1 TEXT NULL
                )
            """)
            conn.commit()
            print("Tabela criada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            conn.close()
