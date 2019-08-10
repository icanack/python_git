import json
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
	variavel = 'Minha Variavel'
	return render_template('index.html')

@app.route('/save', methods = ['POST'])
def save():
        #Comentario qualquer
	dados = request.get_json()
	with open('cache.dat', 'w') as f:
		f.write(json.dumps(dados))
	return jsonify({'mensagem' : 'Dados Gravados'})


@app.route('/status')
def status():
	return jsonify ({'mensagem':'Ola Flask!'})

if __name__ == '__main__':
	app.run(port =5000, debug=True, host='0.0.0.0')
