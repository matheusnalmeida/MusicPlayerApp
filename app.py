from flask import Flask, render_template, request, redirect, url_for, session, g, jsonify, make_response
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
        novoUsuario = User(
            request.form['nome'],
            request.form['usuario'],
            request.form['senha'])

        response = user_service.insert_user(novoUsuario)        
        if response.success:
            response.url = url_for('login')

        return jsonify(response.to_json())

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        return render_template('login.html')
    else:
        response = user_service.login(request.form['usuario'], request.form['senha'])
        if response.success:
            response.url = url_for('index')
            session['logged_user'] = vars(response.data)

        return jsonify(response.to_json()) 

@app.route('/logout/')
def logout():
    session.pop('logged_user')    
    return redirect(url_for('index'))

@app.route('/music-player/')
def music_player():
    return render_template('music-player.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)