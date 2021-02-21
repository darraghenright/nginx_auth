import datetime
import logging
import os

from flask import Flask, redirect, render_template, request, Response
from flask_login import current_user, LoginManager, login_required, login_user, logout_user

from users import FakeUserDatabase

MSG_FORMAT = '%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG, format=MSG_FORMAT)

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = os.environ['FLASK_SECRET_KEY']

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id: str):
    # From the docs:
    #
    # "This callback is used to reload the user object from
    # the user ID stored in the session. It should take the
    # unicode ID of a user, and return the corresponding user
    # object. It should return None (not raise an exception)
    # if the ID is not valid. In that case, the ID will manually
    # be removed from the session and processing will continue."

    user = FakeUserDatabase().find(user_id)

    if not user:
        logging.info(f'Could not find a user with id {user_id}')
    else:
        logging.info(f'Found user: {user}')

    return user

@app.route('/auth', methods=['GET'])
@login_required
def auth():
    # From the docs:
    #
    # "If you decorate a view with this, it will
    # ensure that the current user is logged in
    # and authenticated before calling the actual view"
    #
    # In this scenario, NGINX calls this route to perform
    # the auth sub-request. If successful, we explicitly
    # return a successful HTTP response and set a response
    # header identifying the current user. NGINX will set
    # this `x-auth-user` header on the proxied request it
    # forwards to whatever app is configured to handle the
    # request, and it can use this value to load the user
    # context if required.

    response = Response(status=200)
    response.headers['x-auth-user'] = current_user.id

    return response

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    # @TODO validate login form against
    # some dummy credentials here.
    if request.method == 'POST':
        user = FakeUserDatabase().find('1')
        login_user(user)

        return redirect('/')

    return render_template('login.html')

@app.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect('/auth/login')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
