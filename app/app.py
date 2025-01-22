import socket
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template("index.html", hostname=host_name, ip=host_ip)
    except socket.gaierror:
        return render_template(
            "error.html", message="Unable to resolve hostname to IP address."
        )
    except Exception:  # pylint: disable=broad-except
        return render_template("error.html")


@app.route("/health")
def health():
    return {"is_healthy": True}


@app.route("/user/<user_id>")
def greet_user(user_id):
    return f"hello {user_id}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    print("Service is shutting down..")
