class Armario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tamanho_armario = db.Column(db.String(80), unique=True, nullable=False)
    descricao = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
            return '<User %r>' % self.username
