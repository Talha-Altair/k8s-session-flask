from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_session import Session
from flask_cors import CORS
from datetime import timedelta
import random
import redis

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["secret_key"] = "supersecretkey"
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.from_url('redis://redis-service:6379')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

sess = Session()
sess.init_app(app)
CORS(app)

def random_num():

    num = random.randint(1, 100)

    res = {"num": num}

    return res

@app.route('/login', methods=['GET', 'POST'])
def login():

    username = request.json.get('username')
    password = request.json.get('password')

    print(session.sid)
    

    if password == '1234':

        session['username'] = username
        session['password'] = password

        return jsonify({"num": 1})

    return jsonify({"num": 0})

@app.route('/random', methods=['GET', 'POST'])
def random_route():

    print(session.sid)

    if not session.get('username'):

        return jsonify({"num": 0})

    return jsonify(random_num())

if __name__ == '__main__':

    app.run(debug=True, port=9000, host='0.0.0.0')