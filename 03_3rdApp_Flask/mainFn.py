from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

WebApp = Flask(__name__)

@WebApp.route('/')

def index():
    if not session.get('logged_in'):
        return render_template('loginForm.html')
    else:
        return 'Hello Boss!  <a href="/logout">Logout</a>'

@WebApp.route('/login', methods=['POST'])

def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Usrs).filter(Usrs.username.in_([POST_USERNAME]), Usrs.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()

@WebApp.route('/logout')

def logout():
    session['logged_in'] = False
    return index()

if __name__ == '__main__':
    WebApp.secret_key = os.urandom(12)
    WebApp.run(host='0.0.0.0', port=4000, debug=True)