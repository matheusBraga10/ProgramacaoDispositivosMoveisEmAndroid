class Cadastro_Entregador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(80), unique=True, nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.Integer, unique=True, nullable=False)
    senha1 = db.Column(db.String(120), nullable=False)
    def __repr__(self):
            return '<User %r>' % self.username
