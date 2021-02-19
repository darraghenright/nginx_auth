from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/auth')
def auth():
    return jsonify({'data': 'success'}), 200

@app.route('/reviews')
def cirp_index():
    return render_template('reviews.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=5000)
