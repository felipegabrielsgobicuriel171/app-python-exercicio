from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # A mensagem inicial do seu aplicativo
    message = os.environ.get('WELCOME_MESSAGE', 'Olá do meu aplicativo Python no Azure!')
    return f'<h1>{message}</h1><p>Esta é uma aplicação Flask simples.</p>'

@app.route('/about')
def about():
    return '<h1>Sobre nós</h1><p>Este aplicativo foi criado para demonstrar a implantação no Azure.</p>'

if __name__ == '__main__':
    app.run(debug=True)