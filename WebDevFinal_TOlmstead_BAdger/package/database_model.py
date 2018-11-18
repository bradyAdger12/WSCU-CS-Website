from package import db, login_manager
from flask_login import UserMixin

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

    def __repr__(self):
        return "First Name: " + self.firstname + "  Last Name: " + self.lastname + "  Email: " + self.email + \
            "  Username: " + self.username + "  Password: " + self.password
