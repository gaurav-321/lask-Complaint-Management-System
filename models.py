from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    location = db.Column(db.String, unique=False, nullable=True)
    media = db.Column(db.String, unique=False, nullable=True)

    def __init__(self, title, description, location, media):
        self.title = title
        self.description = description
        self.location = location
        self.media = media

