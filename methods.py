from flask import session, redirect


def login_user(data, role):
    session['logged_in'] = True
    session['username'] = data['username']
    session['password'] = data['password']
    session['dept'] = role


def user_logged():
    if "logged_in" in session.keys() and session['logged_in'] is True:
        return True
    else:
        return False
