from sys import set_coroutine_origin_tracking_depth
from flask import Flask, render_template, request, redirect, url_for
import uuid
from models.user import User
from services.user_service import UserService

app = Flask(__name__)
user_service = UserService()

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
            user_service.insert_user(novoUsuario)

        return redirect(url_for('index'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        return render_template('login.html')
    else:
        usuario = request.form['usuario']
        senha = request.form['senha']
        user = user_service.get_user_by_username_pass(usuario, senha)
        if user != None:
            return redirect(url_for('index'))
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 

# str(uuid.uuid4())