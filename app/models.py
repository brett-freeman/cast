from . import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(100))
    username = db.Column(db.String(1000), unique=True)
    is_admin = db.Column(db.Boolean)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Pick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(140))
    album = db.Column(db.String(140))
    song = db.Column(db.String(140))
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
