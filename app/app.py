import logging
from flask import Flask, render_template

logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    logging.info('/home')
    return render_template('home.html')

@app.route('/reviews')
def cirp_index():
    logging.info('/reviews')
    return render_template('reviews.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
