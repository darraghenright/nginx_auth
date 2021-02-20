import logging
from flask import Flask, render_template

MSG_FORMAT = '%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG, format=MSG_FORMAT)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
