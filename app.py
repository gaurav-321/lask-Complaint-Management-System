from flask import url_for, redirect, Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SECRET_KEY'] = os.urandom(12).hex()

db = SQLAlchemy(app)

if __name__ == '__main__':
    from routes import *
    db.create_all()
    app.run(host="127.0.0.1", port=8080, debug=True, threaded=True)
