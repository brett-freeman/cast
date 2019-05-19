from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))
    is_admin = db.Column(db.Boolean)
    

