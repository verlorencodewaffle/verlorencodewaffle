from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Conexão com MongoDB Atlas
try:
    client = MongoClient("mongodb+srv://atlas-sample-dataset-load-67f9663a49df8e1a7ac8bed2:qff2zxpH9mmFjicL@cluster0.yvp3uw2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["meu_banco"]  # nome do banco que você quiser
    colecao_usuarios = db["usuarios"]  # nome da coleção
except ConnectionFailure as e:
    print(f"Erro ao conectar no MongoDB: {e}")

 
 

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/usuario', methods=['POST'])
def adicionar_usuario():
    data = request.json
    usuario = data.get('usuario')
    senha = data.get('senha')
    dominio = data.get('dominio')

    if not usuario or not senha or not dominio:
        return jsonify({'erro': 'Todos os campos são obrigatórios (usuario, senha, dominio)'}), 400

    usuario_doc = {
        'usuario': usuario,
        'senha': senha,
        'dominio': dominio
    }

    colecao_usuarios.insert_one(usuario_doc)
    return jsonify({'mensagem': 'Usuário adicionado com sucesso'}), 201

@app.route('/xvudqwmzlekrbthgnypcsoijafxvudqwmzlekrbthgnypcsoijafxvudqwmzlekrbthgnypcsoijaf', methods=['GET'])
def listar_usuarios():
    usuarios = list(colecao_usuarios.find({}, {'_id': 0}))
    return jsonify(usuarios), 200


