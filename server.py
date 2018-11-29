#!/usr/bin/python
# coding: utf-8

from flask import Flask, render_template, redirect, url_for, request
import subprocess

# init app
app = Flask(__name__)


# route
@app.route('/')
def home():
    return "home page"


@app.route('/ls')
def get_list():
    msg = subprocess.check_output ('pip install ansible', shell=True)
    return msg


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'a' or request.form['password'] != 'a':
            error = 'Try Again'
        else:
            return redirect(url_for('get_pass'))
    return render_template('index.html', error=error)


@app.route('/pass')
def get_pass():
    return 'Secret'


# start server
if __name__ == "__main__":
    app.run(port=5000, debug=True)
else:
    print("server init fail")
