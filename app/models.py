from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import requests

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
class User(db.Model, UserMixin):
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Data():

    def get_request_ha_international():
        response = requests.get("https://projects.propublica.org/nonprofits/api/v2/organizations/300739799.json")
        if response.status_code == 200:
            international_data = response.json()
            return international_data
        else:
            return None
        

    def get_request_ha_health():
        response = requests.get("https://projects.propublica.org/nonprofits/api/v2/organizations/363775696.json")
        if response.status_code == 200:
            health_data = response.json()
            return health_data
        else:
            return None
        
    def get_request_ha_human_needs():
        response = requests.get("https://projects.propublica.org/nonprofits/api/v2/organizations/361877640.json")
        if response.status_code == 200:
            human_needs_data = response.json()
            return human_needs_data
        else:
            return None

    def get_request_ha_care_services():
        response = requests.get("https://projects.propublica.org/nonprofits/api/v2/organizations/36-4053244.json")
        if response.status_code == 200:
            care_services_data = response.json()
            return care_services_data
        else:
            return None

    def get_request_ha_housing():
        response = requests.get("https://projects.propublica.org/nonprofits/api/v2/organizations/36-3642952.json")
        if response.status_code == 200:
            housing_data = response.json()
            return housing_data
        else:
            return None
        
    # def define_year():

