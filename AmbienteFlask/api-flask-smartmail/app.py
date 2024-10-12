from flask import Flask, request, jsonify
import jose
import dynaconf
import datetime
import sqlite3
import http.client
import json

app = Flask(__name__)


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

@app.route('/cadastro-entregador', methods=['POST'])
def cadastrar_entregador():
    data = request.get_json()

    nome_completo_valor = data.get('nome_completo')
    cpf_valor = data.get('cpf')
    email_valor = data.get('email')
    telefone_valor = data.get('telefone')
    senha1_valor = data.get('senha1')
    senha2_valor = data.get('senha2')

    # Verificar campos obrigatórios
    if not nome_completo_valor or not email_valor or not senha1_valor or not senha2_valor:
        return jsonify({'message': 'Por favor, preencha todos os campos obrigatórios.'}), 400

    # Verificar se as senhas correspondem
    if senha1_valor != senha2_valor:
        return jsonify({'message': 'As senhas digitadas não correspondem.'}), 400

    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        # Verificar se o CPF ou o email já está cadastrado
        cursor.execute("SELECT * FROM Cadastro_Entregador WHERE cpf = ? OR email = ?", (cpf_valor, email_valor))
        if cursor.fetchone() is not None:
            return jsonify({'message': 'CPF ou Email já cadastrado.'}), 409

        # Inserir o novo entregador na tabela Cadastro_Entregador
        cursor.execute("""
            INSERT INTO Cadastro_Entregador (nome_completo, cpf, email, telefone, senha1)
            VALUES (?, ?, ?, ?, ?)
        """, (nome_completo_valor, cpf_valor, email_valor, telefone_valor, senha1_valor))
        conn.commit()

        return jsonify({'message': 'Dados cadastrados com sucesso.'}), 201

    except sqlite3.Error as e:
        return jsonify({'error': f'Erro ao cadastrar dados: {e}'}), 500
    finally:
        conn.close()

@app.route('/criar-tabela-armario', methods=['POST'])
def criar_tabela_armario():
    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        # Criar a tabela Armario
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Armario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tamanho_armario TEXT NOT NULL,
                descricao TEXT NULL
            )
        """)
        conn.commit()
        print("Tabela Armario criada com sucesso.")

        # Dados iniciais para a tabela Armario
        armarios = [
            ('Pequeno', '1'),
            ('Medio', '2')
        ]

        # Inserir os dados na tabela Armario
        cursor.executemany("""
            INSERT INTO Armario (tamanho_armario, descricao)
            VALUES (?, ?)
        """, armarios)
        conn.commit()
        print("Dados inseridos com sucesso.")

        return jsonify({'message': 'Tabela Armario criada e dados inseridos com sucesso.'}), 201

    except sqlite3.Error as e:
        print(f"Erro ao criar tabela ou inserir dados: {e}")
        return jsonify({'error': f"Erro ao criar tabela ou inserir dados: {e}"}), 500

    finally:
        conn.close()

@app.route('/entregas', methods=['GET'])
def listar_entregas():

    entregas = buscar_entregas()
    if entregas:
        return jsonify(entregas), 200
    else:
        return jsonify({'message': 'Nenhuma entrega encontrada'}), 404

@app.route('/criar-tabela-entregas', methods=['POST'])
def criar_tabela_entregas_endpoint():
    try:
        criar_tabela_entregas()
        return jsonify({'message': 'Tabela de entregas criada com sucesso.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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

@app.route('/entregas', methods=['GET'])
def listar_entregas():
    entregas = buscar_entregas()

    if entregas:
        # Formatação dos dados em JSON
        entregas_formatadas = []
        for entrega in entregas:
            entregas_formatadas.append({
                'id': entrega[0],
                'morador_nome': entrega[1],
                'data_entrega': entrega[2],
                'data_retirada': entrega[3],
                'descricao_armario': entrega[4],
                'status_entrega': entrega[5],
                'status_armario': entrega[6]
            })
        return jsonify(entregas_formatadas), 200
    else:
        return jsonify({'message': 'Nenhuma entrega encontrada.'}), 404


def verificar_senha_entregador(senha):
    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Cadastro_Entregador WHERE senha1 = ?", (senha,))
        entregador = cursor.fetchone()
        if entregador:
            return True
        else:
            return False
    except sqlite3.Error as e:
        print(f"Erro ao verificar senha do entregador: {e}")
        return False
    finally:
        conn.close()


@app.route('/verificar-senha-entregador', methods=['POST'])
def verificar_senha():
    dados = request.json
    senha = dados.get('senha')

    if not senha:
        return jsonify({'message': 'Senha não fornecida.'}), 400

    if verificar_senha_entregador(senha):
        return jsonify({'message': 'Senha correta.', 'status': 'success'}), 200
    else:
        return jsonify({'message': 'Senha incorreta.', 'status': 'error'}), 401

@app.route('/confirmar-armario', methods=['POST'])
def confirmar_armario():
    dados = request.json
    tamanho_selecionado = dados.get('tamanho')

    descricao_codigo = None

    # Mapeamento do tamanho do armário para um código de descrição
    if tamanho_selecionado == "Pequeno":
        descricao_codigo = "1"
    elif tamanho_selecionado == "Médio":
        descricao_codigo = "2"

    if not descricao_codigo:
        return jsonify({'message': 'Tamanho inválido.'}), 400

    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        # Verificar se o armário está ocupado
        cursor.execute("""
            SELECT 1 FROM Tabela_de_Entregas 
            WHERE armario_id = ? AND status = 'A retirar'
        """, (descricao_codigo,))
        armario_ocupado = cursor.fetchone()

        if armario_ocupado:
            return jsonify({'message': f'O armário {descricao_codigo} já está sendo usado.'}), 409

        # Verificar se o armário existe
        cursor.execute("SELECT descricao FROM Armario WHERE descricao = ?", (descricao_codigo,))
        resultado = cursor.fetchone()

        if resultado:
            armario_descricao = resultado[0]
            return jsonify({
                'message': 'Armário disponível.',
                'armario_descricao': armario_descricao,
                'descricao_codigo': descricao_codigo
            }), 200
        else:
            return jsonify({'message': 'Armário não encontrado.'}), 404

    except sqlite3.Error as e:
        return jsonify({'message': f'Erro ao buscar armário: {e}'}), 500
    finally:
        conn.close()

@app.route('/buscar-morador', methods=['POST'])
def buscar_morador_por_criterio():
    dados = request.json
    nome = dados.get('nome')
    sobrenome = dados.get('sobrenome')
    telefone = dados.get('telefone')
    N_ap = dados.get('N_ap')
    armario_descricao = dados.get('armario_descricao')
    descricao_codigo = dados.get('descricao_codigo')

    if not criterio:
        return jsonify({'message': 'Critério de busca não informado.'}), 400

    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        # Query para buscar o morador com base no critério fornecido
        query = """
            SELECT nome, sobrenome, N_ap, telefone 
            FROM Cadastro 
            WHERE nome = ? OR sobrenome = ? OR telefone = ? OR N_ap = ?
        """
        cursor.execute(query, (nome, sobrenome, telefone, N_ap))
        moradores_encontrados = cursor.fetchall()

        if not moradores_encontrados:
            return jsonify({'message': f"Nenhum morador encontrado para o '{N_ap}'."}), 404
        else:
            moradores_lista = []
            for morador in moradores_encontrados:
                morador_info = {
                    "nome": morador[0],
                    "sobrenome": morador[1],
                    "N_ap": morador[2],
                    "telefone": morador[3]
                }
                moradores_lista.append(morador_info)

            # Supondo que 'finalizar_processo' gere o código da entrega
            codigo_entrega = finalizar_processo(armario_descricao)

            # Inserir entrega no banco de dados (Função fictícia 'inserir_entrega')
            inserir_entrega(moradores_encontrados[0], descricao_codigo, codigo_entrega)

            return jsonify({
                'message': 'Moradores encontrados.',
                'moradores': moradores_lista,
                'codigo_entrega': codigo_entrega
            }), 200

    except sqlite3.Error as e:
        return jsonify({'message': f"Erro ao buscar morador: {e}"}), 500
    finally:
        conn.close()


@app.route('/inserir-entrega', methods=['POST'])
def inserir_entrega():
    dados = request.json
    morador = dados.get('morador')  # morador deve ser um array ou dicionário com os dados
    descricao_codigo = dados.get('descricao_codigo')
    codigo_entrega = dados.get('codigo_entrega')

    if not morador or not descricao_codigo or not codigo_entrega:
        return jsonify({'message': 'Dados incompletos.'}), 400

    conn = None
    cursor = None

    for attempt in range(5):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()

            # Data da entrega formatada
            data_entrega = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            connHttp = http.client.HTTPSConnection("192.168.0.144")

            connHttp.request("GET", "/")

            # Obtém a resposta
            res = connHttp.getresponse()
            data = res.read()

            # Inserindo a entrega no banco de dados
            cursor.execute("""
                INSERT INTO Tabela_de_Entregas (morador_id, data_entrega, codigo_gerado, status, armario_id)
                VALUES (?, ?, ?, ?, ?)
            """, (morador['id'], data_entrega, codigo_entrega, 'A retirar', descricao_codigo))

            conn.commit()

            return jsonify({
                'message': f"Entrega para {morador['nome']} {morador['sobrenome']} no armário {descricao_codigo}.",
                'status': 'sucesso'
            }), 200

        except sqlite3.OperationalError as e:
            if "database is locked" in str(e):
                print("Banco de dados bloqueado, tentando novamente...")
                time.sleep(1)
            else:
                return jsonify({'message': f"Erro ao inserir entrega: {e}"}), 500
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return jsonify({'message': "Não foi possível acessar o banco de dados após várias tentativas."}), 500

@app.route('/atualizar-entrega', methods=['PUT'])
def atualizar_entrega():
    dados = request.json
    codigo_entrega = dados.get('codigo_entrega')

    if not codigo_entrega:
        return jsonify({'message': 'Código da entrega é obrigatório.'}), 400

    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        # Data atual para a retirada
        data_saida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            UPDATE Tabela_de_Entregas 
            SET data_retirada = ?, status = ? 
            WHERE codigo_gerado = ?
        """, (data_saida, "entregue", codigo_entrega))

        # Verificando se a atualização foi realizada
        if cursor.rowcount == 0:
            return jsonify({'message': 'Código da entrega não encontrado.'}), 404

        conn.commit()
        return jsonify({'message': f"Entrega com código {codigo_entrega} atualizada com sucesso."}), 200

    except sqlite3.Error as e:
        return jsonify({'message': f"Erro ao atualizar entrega: {e}"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/verificar-codigo', methods=['POST'])
def verificar_codigo():
    dados = request.json
    codigo_digitado = dados.get('codigo_gerado')

    if not codigo_digitado:
        return jsonify({'message': 'Código gerado é obrigatório.'}), 400

    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT codigo_gerado FROM Tabela_de_Entregas WHERE codigo_gerado = ?", (codigo_digitado,))
        resultado = cursor.fetchone()

        if resultado:
            cursor.execute("SELECT morador_id, armario_id FROM Tabela_de_Entregas WHERE codigo_gerado = ?", (codigo_digitado,))
            entrega = cursor.fetchone()

            if entrega:
                morador_id, armario_id = entrega
                return jsonify({
                    'message': f"Código {codigo_digitado} encontrado no armário {armario_id}.",
                    'morador_id': morador_id,
                    'armario_id': armario_id
                }), 200
            else:
                return jsonify({'message': 'Dados não encontrados.'}), 404
        else:
            return jsonify({'message': 'Código incorreto.'}), 404

    except sqlite3.Error as e:
        return jsonify({'message': f'Erro ao verificar código: {e}'}), 500
    finally:
        cursor.close()
        conn.close()


@app.route('/atualizar-entrega', methods=['PUT'])
def atualizar_entrega():
    dados = request.json
    codigo_entrega = dados.get('codigo_gerado')

    if not codigo_entrega:
        return jsonify({'message': 'Código gerado é obrigatório.'}), 400

    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()

    try:
        data_saida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            UPDATE Tabela_de_Entregas 
            SET data_retirada = ?, status = ? 
            WHERE codigo_gerado = ?
        """, (data_saida, "entregue", codigo_entrega))

        if cursor.rowcount == 0:
            return jsonify({'message': 'Nenhuma entrega encontrada com esse código.'}), 404

        conn.commit()
        return jsonify({'message': f"Entrega com código {codigo_entrega} atualizada com sucesso."}), 200

    except sqlite3.Error as e:
        return jsonify({'message': f'Erro ao atualizar entrega: {e}'}), 500
    finally:
        cursor.close()
        conn.close()


@app.route('/finalizar-processo/<string:armario_descricao>', methods=['POST'])
def finalizar_processo(armario_descricao):
    codigo_entrega = secrets.choice(range(10000, 100000))
    print(f"Código de Entrega Gerado: {codigo_entrega}")

    return jsonify({
        'message': 'Processo finalizado com sucesso.',
        'codigo_entrega': codigo_entrega,
        'armario_descricao': armario_descricao
    }), 200


if __name__ == '__main__':
    app.run()