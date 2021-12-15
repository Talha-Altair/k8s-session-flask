from flask import Flask, json, render_template, request, redirect, url_for, flash, jsonify
import requests
from requests.sessions import Session
import settings
import json

app = Flask(__name__)

BACKEND_URL = settings.BACKEND_URL

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

    return render_template('index.html', num="logged in successfully")

@app.route('/random', methods=['GET', 'POST'])
def random_route():

    req = requests.get(BACKEND_URL + '/random')

    num = json.loads(req.content.decode('utf-8'))['num']

    if not num:

        return render_template('index.html', num="not logged in")

    return render_template('index.html', num=num)

if __name__ == '__main__':

    app.run(debug=True, port=8000, host='0.0.0.0')