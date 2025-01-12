from flask import Flask, render_template, request, redirect
import json
from datetime import datetime

app = Flask(__name__)

# Função para carregar os nomes do arquivo JSON
def carregar_nomes():
    try:
        with open('nomes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar o nome no arquivo JSON
def salvar_nome(nome):
    nomes = carregar_nomes()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nomes.append({"nome": nome, "data": data_hora})
    with open('nomes.json', 'w') as f:
        json.dump(nomes, f, indent=4)

@app.route('/divirta', methods=['POST'])
def divirta():
    nome = request.form['nome']
    salvar_nome(nome)
    return redirect('/painel')

@app.route('/painel')
def painel():
    nomes = carregar_nomes()
    return render_template('painel.html', nomes=nomes)

@app.route('/')
def pagina1():
    return render_template('pagina1.html')

if __name__ == "__main__":
    app.run(debug=True)
