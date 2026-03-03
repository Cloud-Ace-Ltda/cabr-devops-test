import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Acesso na rota raiz (/)")
    return jsonify({
        "message": "Bem-vindo ao Desafio DevOps GCP!",
        "status": "online"
    }), 200

@app.route('/health')
def health_check():
    # Rota útil para configurar Health Checks em Load Balancers ou GKE
    return jsonify({"status": "healthy"}), 200

@app.route('/data')
def get_data():
    app.logger.info("Tentativa de acesso na rota (/data)")
    
    # A ARMADILHA: Esta rota exige uma variável de ambiente.
    # Serve para testar como o candidato injeta secrets ou configs no GCP.
    api_key = os.environ.get('API_KEY')
    
    if not api_key:
        app.logger.error("Falha: API_KEY não encontrada nas variáveis de ambiente.")
        return jsonify({"error": "Internal Server Error - Missing Configuration (API_KEY)"}), 500
    
    return jsonify({
        "message": "Acesso autenticado com sucesso!", 
        "api_key_masked": f"{api_key[:3]}***" # Mostra só os 3 primeiros caracteres
    }), 200

if __name__ == '__main__':
    # O Cloud Run espera que a aplicação rode na porta especificada pela variável PORT.
    # O padrão é 8080, mas o candidato precisa garantir que isso funciona.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
