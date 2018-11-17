from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login_account', methods=['GET', 'POST'])
def login_account():
    return render_template("LoginAccount.html")

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    return render_template("CreateAccount.html")


if __name__ == '__main__':
    app.run(debug=True)
