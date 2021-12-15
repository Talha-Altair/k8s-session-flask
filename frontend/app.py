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

    if req.content == b'0':

        flash('Wrong username or password!')

        return redirect(url_for('index'))

    print(Session)

    num = json.loads(req.content.decode('utf-8'))['num']

    return render_template('index.html', num=num)