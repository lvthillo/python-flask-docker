from flask import Flask,render_template
import socket
import time
from codeguru_profiler_agent import Profiler
import boto3

app = Flask(__name__)

@app.route("/")
def index():
    try:
        # host_name = socket.gethostname()
        # host_ip = socket.gethostbyname(host_name)
        host_name = 'hellen'
        host_ip = '123'
        host_ip = 'test'
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')

# def load_kinesis_record():
#     kinesis_record = None
#     try:
#         if kinesis_record == 1:
#             kinesis_record = subprocess.call(cmd, shell=True)
#         else:
#             kinesis_record = eval(cmd)
#         successes += 1
#     except Exception as e:
#         pass
#     return kinesis_record


if __name__ == "__main__":
    custom_session = boto3.session.Session(profile_name='dev', region_name='us-west-2')
    Profiler(profiling_group_name="PythonProfiler", aws_session=custom_session).start()
    start_application()
    app.run(host='0.0.0.0', port=8080)
