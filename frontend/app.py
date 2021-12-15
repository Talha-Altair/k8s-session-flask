from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

BACKEND_URL = 'http://

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == 'admin':

        flash('Login successful.')

        return redirect(url_for('index'))

    return render_template('error.html')