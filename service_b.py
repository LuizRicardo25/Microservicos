from flask import Flask
app = Flask(__name__)

@app.route('/get-message')
def get_message():
    return 'Mensagem do Serviço B'

if __name__ == '__main__':
    app.run(port=5001)
