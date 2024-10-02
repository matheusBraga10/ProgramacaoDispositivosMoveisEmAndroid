class Tabela_de_Entregas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    morador_id = db.Column(db.Integer, unique=True, nullable=False, foreign_key=True)
    data_entrega = db.Column(db.DateTime, unique=True, nullable=False)
    data_retirada = db.Column(db.DateTime, unique=True, nullable=False)
    codigo_gerado = db.Column(db.Integer, unique=True, nullable=False)
    status = db.Column(db.String(80), unique=True, nullable=False)
    armario_id = db.Column(db.Integer, unique=True, nullable=False, foreign_key=True)
    def __repr__(self):
            return '<User %r>' % self.username
