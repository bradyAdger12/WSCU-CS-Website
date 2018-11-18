from flask import Flask, render_template, redirect, url_for, send_from_directory
from package.AccountForms import FormCreateAccount, FormLogin
from package import app
from package import bcrypt
from package import db
from package.database_model import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    #if current_user.is_authenticated():
    #    return redirect(url_for('home'))
    form = FormCreateAccount()
    #print("Test")
    if form.validate_on_submit():
        print("Hello World!!!")
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data,
                    username=form.username.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        return redirect(url_for('home'))

    return render_template("CreateAccount.html", form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated():
    #    return redirect(url_for('home'))
    form = FormLogin()
    if form.validate_on_submit():
        print("Login Successful!")
        user = User.query.filter_by(email=form.email.data).first()
        check_password = bcrypt.check_password_hash(user.password, form.password.data)
        if user and check_password:
            login_user(user, form.remember_me.data)
            return redirect(url_for('home'))
    return render_template("LoginAccount.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("Home.html")

@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('Account.html')

