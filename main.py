from flask import Flask, request, jsonify
from flask_cors import CORS  # Evita bloqueos de seguridad del navegador

app = Flask(__name__)
CORS(app)  # Permite que el HTML local hable con Python

@app.route('/sumar', methods=['POST'])
def sumar():
    # Recibimos los datos enviados desde el HTML
    datos = request.get_json()

    num1 = float(datos.get('n1', 0))
    num2 = float(datos.get('n2', 0))

    resultado = num1 + num2

    # Devolvemos la respuesta en formato JSON
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    # Arrancamos el servidor en el puerto 5000
    app.run(host='0.0.0.0', port=5000)