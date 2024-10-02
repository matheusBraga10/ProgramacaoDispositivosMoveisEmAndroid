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
    def __repr__(self):
            return '<User %r>' % self.username
