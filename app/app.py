import logging
from functools import wraps
from flask import abort, Flask, g, render_template, request

MSG_FORMAT = '%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(filename='/srv/logs/access.log', level=logging.DEBUG, format=MSG_FORMAT)

app = Flask(__name__)

def load_user(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # Create an explicit `@load_user` decorator, rather than
        # use a Flask hook like `@app.before_request` because there
        # might requests that don't need or don't have a concept of
        # the `x-auth-user` header. In this scenario, static assets
        # are an example as they are not authenticated by NGINX.

        user_id = request.headers.get('x-auth-user')

        # Here we would use the user id value provided in the `x-auth-user`
        # header and attempt to load their identity from from a db or cache
        # and make sure that they are a valid, active user via that mechanism.
        # If the id didn't happen to match, or the user was locked/deactivated
        # we can abort the request and block them here, or we could redirect
        # them to `/auth/login` explicitly. Or maybe it would be possible to
        # configure NGINX to perform a redirect on receipt of a 40* response
        # status and allow any upstream applications to be unaware for the
        # implementation details of the auth later.

        if not user_id:
            abort(403)

        # But in this example we pretend we know the user so let's
        # set a global user object that we can use in route functions
        # and view templates!

        # @TODO mockout/lookup a user here
        g.user = {
            'id': user_id,
            'email': 'bob@example.com',
            'name': 'Bob'
        }

        return f(*args, **kwargs)

    return decorator

@app.route('/')
@load_user
def home():
    return render_template('home.html')

@app.route('/reviews')
@load_user
def reviews():
    return render_template('reviews.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
