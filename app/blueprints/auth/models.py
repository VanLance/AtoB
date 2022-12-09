from app import db, login
from flask_login import UserMixin
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    # __table__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String, nullable=False)
    token = db.Column(db.String, unique=True, index=True)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    user_service = db.relationship('Service', backref='owner', lazy=True)
    user_additional = db.relationship('Additional', backref='extra_owner', lazy=True)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.id}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    # salt and hash our password to make it hard to steal
    def hash_password(self, original_password):
        self.password = generate_password_hash(original_password)

    def check_password(self, login_password):
        return check_password_hash(self.password, login_password)   


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
        