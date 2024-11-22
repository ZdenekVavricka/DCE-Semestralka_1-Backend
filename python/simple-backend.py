#
# Simple backend service
#

from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return '<html><head><title>Backend Service</title></head>' + \
           '<body><h1>Welcome to Python Server</h1>'+ \
           '<p><b>Served by: </b><mark>'+ \
           socket.gethostname() + '</mark></p></body></html>\n'

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# EOF