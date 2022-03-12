from flask import Flask, render_template, request, redirect, url_for, session, g
from models.user import User
from services.user_service import UserService
from utils.util import valid_acess

app = Flask(__name__)
SECRET_KEY = 'ffa210c9-33f8-4966-b1f6-8c65e28c3bd1'
app.secret_key = SECRET_KEY

user_service = UserService()

@app.before_request
def before_request():
    g.logged_user = None
    acessNotValid = not valid_acess(request)
    if(acessNotValid):
        return redirect(url_for('index'))
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if(request.method == 'GET'):
        return render_template('register.html')
    else:
        nome = request.form['nome']
        usuario = request.form['usuario']
        senha = request.form['senha']

        novoUsuario = User(nome, usuario, senha)
        if(novoUsuario.is_valid()):
            user_service.insert_user(novoUsuario)

        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        return render_template('login.html')
    else:
        usuario = request.form['usuario']
        senha = request.form['senha']
        user = user_service.get_user_by_username_pass(usuario, senha)
        if user:
            session['logged_user'] = vars(user)
            return redirect(url_for('index'))
    
    return redirect(url_for('index'))

@app.route('/logout/')
def logout():
    session.pop('logged_user')    
    return redirect(url_for('index'))

@app.route('/music-player/')
def music_player():
    return render_template('music-player.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 

# str(uuid.uuid4())