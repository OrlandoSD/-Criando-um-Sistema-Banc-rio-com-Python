from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Variáveis globais para simular o banco de dados
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/depositar', methods=['POST'])
def depositar():
    global saldo, extrato
    valor = request.json.get('valor')
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return jsonify({"mensagem": "Depósito realizado com sucesso", "saldo": saldo}), 200
    else:
        return jsonify({"mensagem": "Operação falhou! O valor informado é inválido."}), 400

@app.route('/sacar', methods=['POST'])
def sacar():
    global saldo, extrato, numero_saques
    valor = request.json.get('valor')
    if valor > saldo:
        return jsonify({"mensagem": "Operação falhou! Você não tem saldo suficiente."}), 400
    elif valor > limite:
        return jsonify({"mensagem": "Operação falhou! O valor do saque excede o limite."}), 400
    elif numero_saques >= LIMITE_SAQUES:
        return jsonify({"mensagem": "Operação falhou! Número máximo de saques excedido."}), 400
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return jsonify({"mensagem": "Saque realizado com sucesso", "saldo": saldo}), 200
    else:
        return jsonify({"mensagem": "Operação falhou! O valor informado é inválido."}), 400

@app.route('/extrato', methods=['GET'])
def ver_extrato():
    global extrato, saldo
    return jsonify({"extrato": extrato, "saldo": saldo}), 200

if __name__ == '__main__':
    app.run(debug=True)
