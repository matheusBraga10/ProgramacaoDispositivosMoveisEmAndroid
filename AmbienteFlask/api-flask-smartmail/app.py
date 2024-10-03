from flask import Flask, request, jsonify
import jose
import dynaconf
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.MODIFICATIONS
app.config['SECRET_KEY'] = settings.SECRET_KEY

@app.route('/login', methods=['POST'])
def verificar_login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Cadastro WHERE email=? AND senha1=?", (email, senha))
        user = cursor.fetchone()
        if user:
            return jsonify({'message': 'Login correto!', 'user': user}), 200
        else:
            return jsonify({'message': 'Login inválido.'}), 401
    except sqlite3.Error as e:
        return jsonify({'error': f"Erro: {e}"}), 500
    finally:
        conn.close()

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    data = request.get_json()

    nome_valor = data.get('nome')
    sobrenome_valor = data.get('sobrenome')
    cpf_valor = data.get('cpf')
    email_valor = data.get('email')
    telefone_valor = data.get('telefone')
    cep_valor = data.get('cep')
    rua_valor = data.get('rua')
    N_ap_valor = data.get('N_ap')
    numero_valor = data.get('numero')
    bairro_valor = data.get('bairro')
    cidade_valor = data.get('cidade')
    estado_valor = data.get('estado')
    senha1_valor = data.get('senha1')

    if not nome_valor or not sobrenome_valor or not email_valor or not senha1_valor or not senha2_valor:
        return jsonify({'message': 'Por favor, preencha todos os campos obrigatórios.'}), 400

    if senha1_valor != senha2_valor:
        return jsonify({'message': 'As senhas digitadas não correspondem.'}), 400

    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO Cadastro (nome, sobrenome, cpf, email, telefone, cep, rua, N_ap, numero, bairro, cidade, estado, senha1)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome_valor, sobrenome_valor, cpf_valor, email_valor, telefone_valor, cep_valor, rua_valor, N_ap_valor, numero_valor, bairro_valor, cidade_valor, estado_valor, senha1_valor))
        conn.commit()
        return jsonify({'message': 'Dados cadastrados com sucesso.'}), 201
    except sqlite3.Error as e:
        return jsonify({'error': f"Erro ao cadastrar dados: {e}"}), 500
    finally:
        conn.close()

# Endpoint para buscar as entregas
@app.route('/entregas', methods=['GET'])
def listar_entregas():

    entregas = buscar_entregas()
    if entregas:
        return jsonify(entregas), 200
    else:
        return jsonify({'message': 'Nenhuma entrega encontrada'}), 404

# Endpoint para criar a tabela de entregas (pode ser usado uma vez para inicialização)
@app.route('/criar-tabela-entregas', methods=['POST'])
def criar_tabela_entregas_endpoint():
    try:
        criar_tabela_entregas()
        return jsonify({'message': 'Tabela de entregas criada com sucesso.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Cria a tabela de entregas na inicialização
    app.run()