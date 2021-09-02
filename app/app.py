from flask import Flask,render_template
import socket
import time
app = Flask(__name__)

@app.route("/")
def index():

    try:
        # host_name = socket.gethostname()
        # host_ip = socket.gethostbyname(host_name)
        host_name = 'hellen'
        host_ip = '123'
        host_ip = 'test'
        calcular_media()
        time.sleep(50)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')
def calcular_media():
    nome = 'Felipe'
    primeira_prova = 10
    segunda_prova = 9
    soma_notas = primeira_prova + segunda_prova + primeira_prova + segunda_prova + primeira_prova + segunda_prova + primeira_prova + segunda_prova +primeira_prova + segunda_prova +primeira_prova + segunda_prova
    quantidade_provas = 2
    return soma / quantidade_provas

def calcular_media():
    nome = 'Felipe'
    primeira_prova = 10
    segunda_prova = 9
    soma_notas = primeira_prova + segunda_prova + primeira_prova + segunda_prova + primeira_prova + segunda_prova + primeira_prova + segunda_prova +primeira_prova + segunda_prova +primeira_prova + segunda_prova
    quantidade_provas = 2
    return soma / quantidade_provas

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
