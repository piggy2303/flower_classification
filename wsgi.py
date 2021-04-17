from gevent.pywsgi import WSGIServer
from index_api import app


import os

PORT = int(os.getenv('PORT', '5003'))


if __name__ == '__main__':
    print("done")
    http_server = WSGIServer(('0.0.0.0', PORT), app)
    http_server.serve_forever()
