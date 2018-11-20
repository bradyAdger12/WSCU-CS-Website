from flask import Flask, render_template, redirect, url_for, request, flash, get_flashed_messages
from package.AccountForms import FormCreateAccount, FormLogin, FormUpdateAccount, FormDeleteAccount
from package import app
from package import bcrypt
from package import db
from package.database_model import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if current_user.is_authenticated:
        print("Authenticated")
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        print("Authenticated")
        return redirect(url_for('home'))
    form = FormLogin()
    if form.validate_on_submit():
        print("Login Successful!")
        user = User.query.filter_by(email=form.email.data).first()
        check_password = bcrypt.check_password_hash(user.password, form.password.data)
        if user and check_password:
            login_user(user, form.remember_me.data)
            return redirect(url_for('home'))
        else:
            print("Unsuccessful login check email and password.")
            return redirect(url_for('login'))
    return render_template("LoginAccount.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        select_options = request.form['select']
        select_language = request.form['language_select']
        if select_options == "Data Structures" and select_language == 'None':
            return redirect(url_for('data_structures'))
        elif select_options == "Databases" and select_language == 'None':
            return redirect(url_for('databases'))
        elif select_options == "Graphics" and select_language == 'None':
            return redirect(url_for('graphics'))
        elif select_options == "Data Structures" and select_language == "SQL":
            flash('SQL does not support Data Structures.  Select a different language!', 'success')
            return redirect(url_for('home'))#redirect home because no one does data structures in sql
        elif select_options == "Databases" and select_language == 'SQL':
            return redirect(url_for('sql_database'))
        elif select_options == "Graphics" and select_language == 'SQL':
            flash('SQL does not support graphics.  Select a different language!')
            return redirect(url_for('home'))#redirect home because no one does graphics in sql
        elif select_options == "Data Structures" and select_language == "Python":
            return redirect(url_for('python_ds'))
        elif select_options == "Data Structures" and select_language == "Java":
            return redirect(url_for('java_ds'))
        elif select_options == "Data Structures" and select_language == "C++":
            return redirect(url_for('c_plus_plus_ds'))
        elif select_options == "Databases" and select_language == "Python":
            return redirect(url_for('python_db'))
        elif select_options == "Databases" and select_language == "Java":
            return redirect(url_for('java_db'))
        elif select_options == "Databases" and select_language == "C++":
            return redirect(url_for('c_plus_plus_db'))
        elif select_options == "Graphics" and select_language == "Python":
            return redirect(url_for('python_graphics'))
        elif select_options == "Graphics" and select_language == "Java":
            return redirect(url_for('java_graphics'))
        elif select_options == "Graphics" and select_language == "C++":
            return redirect(url_for('c_plus_plus_graphics'))


    return render_template("Home.html", form=request.form)

@app.route('/account', methods=['GET', 'POST'])
def account():
    form = FormUpdateAccount()
    delete_form = FormDeleteAccount()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    if delete_form.validate_on_submit():
        db.session.delete(current_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('Account.html', form=form, delete_form=delete_form)





