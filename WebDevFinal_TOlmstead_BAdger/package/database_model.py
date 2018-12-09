from package import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=True)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Posts', backref='user')
    #posts_id = db.relationship('Posts', backref='user', foreign_keys='Posts.owner_id')


    def __repr__(self):
        return "First Name: " + self.firstname + "  Last Name: " + self.lastname + "  Email: " + self.email + \
            "  Username: " + self.username + "  Password: " + self.password

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(100), nullable=False)
    post_time = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow())
    #owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner_name = db.Column(db.String, db.ForeignKey('user.username'))

    def __repr__(self):
        return self.post + " " + str(self.post_time)

