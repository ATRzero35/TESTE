from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Dados em memória (substitua depois pelo SharePoint)
registros = []

@app.route('/submit', methods=['POST'])
def submit():
    try:
        dados = request.json
        id_unico = f"{dados.get('operacao', 'OPCAO1')}-{len(registros)+1:04d}"
        
        registro = {
            "id": id_unico,
            "nome": dados.get('nome', ''),
            "operacao": dados.get('operacao', ''),
            "data": datetime.now().isoformat()
        }
        
        registros.append(registro)
        return jsonify({"success": True, "id_unico": id_unico})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "API Simplificada Funcionando! Use POST /submit"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)