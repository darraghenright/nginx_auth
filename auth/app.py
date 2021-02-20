import logging
from flask import Flask, jsonify

MSG_FORMAT = '%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG, format=MSG_FORMAT)

app = Flask(__name__)

@app.route('/auth')
def auth():
    logging.info('serving `/auth`')
    return jsonify(), 401

@app.route('/auth/login')
def login():
    logging.info('serving `/auth/login`')
    return jsonify({'message': 'login page'}), 200

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
