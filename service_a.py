from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Olá do Serviço A'

@app.route('/call-service-b')
def call_service_b():
    response = requests.get('http://localhost:5001/get-message')
    return 'Serviço A chamando Serviço B: ' + response.text

if __name__ == '__main__':
    app.run(port=5000)
