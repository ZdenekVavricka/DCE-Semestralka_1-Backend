#
# Simple backend service demo
#

from flask import Flask
import socket

app = Flask(__name__)

def get_backend_signature():
    return '\n<i>Served by: ' + socket.gethostname() + '<i>\n'

@app.route('/')
def home():
    return '<html><head><title>Backend Service</title></head>' + \
           '<body>' + \
           get_backend_signature() + '</body></html>\n'

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# EOF