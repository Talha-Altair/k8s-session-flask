from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from datetime import timedelta
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

    if password == '1234':

        return jsonify({"num": 1})

    return jsonify({"num": 0})

@app.route('/random', methods=['GET', 'POST'])
def random_route():

    return jsonify(random_num())

if __name__ == '__main__':

    app.run(debug=True, port=9000, host='0.0.0.0')