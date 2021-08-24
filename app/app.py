from flask import Flask,render_template
import socket

app = Flask(__name__)

@app.route("/")
def index():
    try:
        # host_name = socket.gethostname()
        # host_ip = socket.gethostbyname(host_name)
        host_name = 'hellen'
        host_ip = '123'
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
