class Cadastro_Entregador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(80), unique=True, nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.Integer, unique=True, nullable=False)
    senha1 = db.Column(db.String(120), nullable=False)
    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Cadastro_Entregador (
                    id INTEGER PRIMARY KEY,
                    nome_completo TEXT NOT NULL,
                    cpf INTEGER UNIQUE,
                    email TEXT UNIQUE NOT NULL,
                    telefone INTEGER,
                    senha1 TEXT NOT NULL
                )
            """)
            conn.commit()
            print("Tabela criada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            conn.close()


    def cadastrar(self):
        nome_completo_valor = self.entry_nome_completo.get()
        cpf_valor = self.cpf_entry.get()
        email_valor = self.email_entry.get()
        telefone_valor = self.telefone_entry.get()
        senha1_valor = self.senha1_entry.get()
        senha2_valor = self.senha2_entry.get()

        if nome_completo_valor == "" or email_valor == "" or senha1_valor == "" or senha2_valor == "":
            print("Por favor, preencha todos os campos obrigatórios.")
            return

        if senha1_valor != senha2_valor:
            print("As senhas digitadas não correspondem.")
            return

        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM Cadastro_Entregador WHERE cpf = ? OR email = ?", (cpf_valor, email_valor))
            if cursor.fetchone() is not None:
                print("CPF ou Email já cadastrado.")
                return

            cursor.execute("""
                INSERT INTO Cadastro_Entregador (nome_completo, cpf, email, telefone, senha1)
                VALUES (?, ?, ?, ?, ?)
            """, (nome_completo_valor, cpf_valor, email_valor, telefone_valor, senha1_valor))
            conn.commit()
            print("Dados cadastrados com sucesso.")

            self.janela.destroy()
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar dados: {e}")
        finally:
            conn.close()
