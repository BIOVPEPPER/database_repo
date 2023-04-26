from app import db


class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String, unique=True)    
    password = db.Column(db.String)
    isDriver = db.Column(db.Integer)

