import logging
from flask import Flask, jsonify, render_template

MSG_FORMAT = '%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG, format=MSG_FORMAT)

app = Flask(__name__)

@app.route('/auth')
def auth():
    return jsonify(), 401

@app.route('/auth/login')
def login():
    return render_template('login.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
