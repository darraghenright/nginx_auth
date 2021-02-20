import datetime
import logging
import os

from flask import Flask, redirect, render_template, request, Response
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin

MSG_FORMAT = '%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG, format=MSG_FORMAT)

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = os.environ['FLASK_SECRET_KEY']

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id=1):
        self.id = id

    def get_id(self) -> str:
        return str(self.id)

@login_manager.user_loader
def load_user(_user_id):
    return User()

@app.route('/auth', methods=['GET'])
@login_required
def auth():
    return Response(status=200)

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    # @TODO validate login form against
    # some dummy credentials here.
    if request.method == 'POST':
        login_user(user=User(),
                   duration=datetime.timedelta(days=1),
                   force=True,
                   fresh=True,
                   remember=True)

        return redirect('/')

    return render_template('login.html')

@app.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect('/auth/login')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
