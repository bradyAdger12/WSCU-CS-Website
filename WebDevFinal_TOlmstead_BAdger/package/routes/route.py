from flask import Flask, render_template
from package import app


@app.route('/')
@app.route('/login_account', methods=['GET', 'POST'])
def login_account():
    return render_template("LoginAccount.html")

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    return render_template("CreateAccount.html")
