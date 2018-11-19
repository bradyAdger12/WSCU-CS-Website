from flask import render_template, redirect, request
from package import app

@app.route('/python', methods=['GET', 'POST'])
def python():
    return render_template("Languages/Python.html")
@app.route('/c_plus_plus', methods=['GET', 'POST'])
def c_plus_plus():
    return render_template("Languages/C++.html")
@app.route('/c_sharp', methods=['GET', 'POST'])
def c_sharp():
    return render_template("Languages/C#.html")
@app.route('/html', methods=['GET', 'POST'])
def html():
    return render_template("Languages/HTML.html")
@app.route('/java', methods=['GET', 'POST'])
def java():
    return render_template("Languages/Java.html")
@app.route('/javascript', methods=['GET', 'POST'])
def javascript():
    return render_template("Languages/JavaScript.html")
@app.route('/data_structures', methods=['GET', 'POST'])
def data_structures():
    return render_template("Languages/Topics/DataStructures/DataStructures.html")
@app.route('/databases', methods=['GET', 'POST'])
def databases():
    return render_template("Languages/Topics/Databases/Databases.html")