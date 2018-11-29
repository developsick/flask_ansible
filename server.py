#!/usr/bin/python3.7
# coding: utf-8

from flask import Flask, render_template, redirect, url_for, request
import subprocess
import sh

#initialize global variables
port = 5000
host = 'http://127.0.0.1:'+str(port)


# init app
app = Flask(__name__)


def get_href(prefix, addr, refstr):
    return prefix + "<a href=\"" + addr + "\">" + refstr + "</a>"


@app.route('/')
def home():
    # msg = sh.pwd()
    msg = 'Home page'
    return str(msg)


@app.route('/install')
def install_ansible():
    msg = subprocess.check_output('pip install ansible', shell=True)
    return msg

@app.route('/start', methods=['GET', 'POST'])
def start():
    msg = None
    if request.method == 'POST':
        #redirect(url_for('install_ansible'))
        msg = subprocess.check_output('pip install ansible', shell=True)
    return render_template('install_ansible.html', msg=msg)


@app.route('/ls')
def get_list():
    msg = subprocess.check_output ('ls -al', shell=True)
    return msg + get_href('<br/><br/>', host+'/pwd', 'pwd')
    # '''
    # <br/><br/><a href="http://localhost:5000/pwd">pwd</a>
    # '''


@app.route('/pwd')
def get_pwd():
    return str(sh.pwd())


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
    app.run(port=port, debug=True)
else:
    print("server init fail")