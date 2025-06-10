from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Alteração aqui:
    message = os.environ.get('WELCOME_MESSAGE', 'Olá! O aplicativo Python no Azure foi atualizado com sucesso!')
    return f'<h1>{message}</h1><p>Esta é uma aplicação Flask simples.</p>'

@app.route('/about')
def about():
    return '<h1>Sobre nós</h1><p>Este aplicativo foi criado para demonstrar a implantação no Azure.</p>'

if __name__ == '__main__':
    app.run(debug=True)