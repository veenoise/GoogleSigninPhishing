from dotenv import load_dotenv
from flask import Flask, request, render_template, session, redirect, url_for
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY").encode('utf-8')


@app.route("/", methods=['GET', 'POST'])
def index():
    if 'email' in session:
        session.pop('email', None)

    if 'password' in session:
        session.pop('password', None)

    if request.method == 'POST':
        email = request.get_json()
        session['email'] = email['email']
        print(session['email'])
    
    return render_template('email-old.html')

@app.route("/password", methods=['GET', 'POST'])
def password():
    if 'email' not in session:
        return redirect(url_for('index'))

    if 'password' in session:
        session.pop('password', None)

    if request.method == 'POST':
        password = request.get_json()
        session['password'] = password['password']
        print(session['password'])
    
    return render_template('password-old.html')