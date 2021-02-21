import logging
from flask import Flask, g, render_template, request

MSG_FORMAT = '%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG, format=MSG_FORMAT)

app = Flask(__name__)

@app.before_request
def hydrate_user_from_request():
    # this runs before every request. lookup the
    # user from their id from db or cache here.
    g.user = {
        'id': request.headers['x-auth-user'],
        'email': 'bob@example.com',
        'name': 'Bob'
    }

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
