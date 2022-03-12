from flask import Flask, render_template, request, redirect, url_for
from data.memory_database import MemoryDatabase
import uuid

from models.user import User

database = MemoryDatabase.instance()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if(request.method == 'GET'):
        return render_template('register.html')
    else:
        id = str(uuid.uuid4())
        nome = request.form['nome']
        usuario = request.form['usuario']
        senha = request.form['senha']

        novoUsuario = User(id, nome, usuario, senha)
        if(novoUsuario.is_valid()):
            database.users_table[id] = novoUsuario

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 

# str(uuid.uuid4())