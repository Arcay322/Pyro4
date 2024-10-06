from flask import Flask, render_template, request
import Pyro4

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/factorial', methods=['POST'])
def calcular_factorial():
    numero = int(request.form['numero'])
    factorial_server = Pyro4.Proxy("PYRONAME:example.factorial")
    try:
        resultado = factorial_server.factorial(numero)
        return render_template('index.html', resultado=f"El factorial de {numero} es: {resultado}")
    except Exception as e:
        return render_template('index.html', resultado=f"Error al calcular el factorial: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
