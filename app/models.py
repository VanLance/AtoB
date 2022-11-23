from app import db, login
from flask_login import UserMixin
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    # __table__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    user_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    service = db.relationship('Service', backref='owner', lazy=True)

    def __repr__(self):
        return f'{self.user_name}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
        
class Service(db.Model):
    # __table__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    square_foot = db.Column(db.Integer, nullable=False)
    requested_service = db.Column(db.Integer, nullable=False)
    extra = db.Column(db.String)
    user = db.Column(db.ForeignKey('user.id'), nullable=False)

    costs = {
            600: {'weekly': 49, 'biweekly': 59, 'deepClean': 150},
            1000: {'weekly': 79, 'biweekly': 89, 'deepClean': 179},
            1200: {'weekly': 89, 'biweekly': 99, 'deepClean': 189},
            1500: {'weekly': 89, 'biweekly': 99, 'deepClean': 199},
            1800: {'weekly': 105, 'biweekly': 109, 'deepClean': 229},
            2000: {'weekly': 119, 'biweekly': 129, 'deepClean': 249},
            2500: {'weekly': 159, 'biweekly': 169, 'deepClean': 300},
            3000: {'weekly': 199, 'biweekly': 219, 'deepClean': 450},
            4000: {'weekly': 279, 'biweekly': 299, 'deepClean': 600},
            5000: {'weekly': 349, 'biweekly': 369, 'deepClean': 799},
            6000: {'weekly': 429, 'biweekly': 449, 'deepClean': 999},
        }
    
    def estimate(self):
        return self.costs[self.square_foot][self.requested_service]

    def commit(self):
        db.session.add(self)
        db.session.commit()

class Additional(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    polish = db.Column(db.Boolean)
    cabinets = db.Column(db.Boolean)
    baseBoards = db.Column(db.Boolean)
    fridge = db.Column(db.Boolean)
    windows = db.Column(db.Boolean)
    skylights = db.Column(db.Boolean)
    carpetShampoo = db.Column(db.Boolean)
    
    extras = {
        'polishing': 25,
        'cabinets': 20,
        'baseBoards': 25,
        'refridgerator': 15,
        'windows': 4,
        'skylights': 8,
        'carpetShampoo': 40,
    }

    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    # def total(self):

