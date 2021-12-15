from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import random

app = Flask(__name__)

def random_num():

    num = random.randint(1, 100)

    res = {"num": num}

    return res

@app.route('/login', methods=['GET', 'POST'])
def login():

    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'admin' and password == 'admin':

        return jsonify(random_num)

    return 0