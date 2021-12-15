from flask import Flask, json, render_template, request, redirect, url_for, flash, jsonify, session
import requests
import settings
import json
from datetime import timedelta

app = Flask(__name__)

BACKEND_URL = settings.BACKEND_URL

app.config['SECRET_KEY'] = 'xxxxxxxxx'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(seconds=5)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    req = requests.post(BACKEND_URL + '/login', json={'username': username, 'password': password})

    num = json.loads(req.content.decode('utf-8'))['num']

    if num == 0:

        return render_template('index.html', num="wrong password") 

    session.permanent = True

    session['username'] = username

    return render_template('index.html', num="logged in successfully")

@app.route('/random', methods=['GET', 'POST'])
def random_route():

    if 'username' not in session:

        return render_template('index.html', num="please login")

    req = requests.get(BACKEND_URL + '/random')

    num = json.loads(req.content.decode('utf-8'))['num']

    if not num:

        return render_template('index.html', num="not logged in")

    return render_template('index.html', num=num)

if __name__ == '__main__':

    app.run(debug=True, port=8000, host='0.0.0.0')