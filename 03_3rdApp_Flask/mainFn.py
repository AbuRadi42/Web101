from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///matcha.db', echo=True)

WebApp = Flask(__name__)

@WebApp.route('/')

def index():
    if not session.get('logged_in'):
        return render_template('loginForm.html')
    else:
        return render_template('dashBoard.html')

@WebApp.route('/login', methods=['POST'])

def login():
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

@WebApp.route('/signup', methods=['POST'])

def signup():
    POST_USERNAME = str(request.form['username'])
    POST_REALNAME = str(request.form['realname'])
    POST_PASSWORD = str(request.form['password'])
    POST_REPEAT = str(request.form['repeat'])
    POST_E_MAIL = str(request.form['e_mail'])
    POST_GENDER = int(request.form['gender'])
    POST_SEXUALITY = str(request.form['sexuality'])
    POST_BIOGRAPHY = str(request.form['biography'])
    POST_INTERESTS = str(request.form['interests'])
    Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    WebApp.secret_key = os.urandom(12)
    WebApp.run(host='0.0.0.0', port=4000, debug=True)