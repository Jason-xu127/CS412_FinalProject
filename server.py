from flask import Flask, request
import subprocess
import socket
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py.py'])
        return 'Hello, POST'
    else:
        address = socket.gethostname()
        return address