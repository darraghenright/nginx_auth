import logging
from flask import Flask, jsonify

logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/auth')
def auth():
    logging.info('/auth')
    return jsonify({'message': 'forbidden'}), 401

@app.route('/login')
def login():
    logging.info('/login')
    return jsonify({'data': 'login'}), 200

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
