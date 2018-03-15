from flask import Flask
from flask_cors import CORS
import socket
import urllib.request
from flask import jsonify

app = Flask(__name__)
CORS(app)

publicIP = {}


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/network/localIP')
def local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        #s.connect(('10.255.255.255', 1))
        s.connect(('192.168.1.1', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return jsonify(IP)


@app.route('/network/publicIP')
def public_ip():
    # TODO cache
    data = urllib.request.urlopen('https://api.ipify.org').read()
    publicIP['ip'] = str(data, encoding='utf-8')
    return jsonify(publicIP['ip'])
