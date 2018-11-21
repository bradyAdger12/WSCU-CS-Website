from flask import render_template, redirect, request
from package import app
from flask_login import login_required

@app.route('/python', methods=['GET', 'POST'])
@login_required
def python():
    return render_template("Languages/Syntax/Python.html")
@app.route('/c_plus_plus', methods=['GET', 'POST'])
@login_required
def c_plus_plus():
    return render_template("Languages/Syntax/C++.html")
@app.route('/c_sharp', methods=['GET', 'POST'])
@login_required
def c_sharp():
    return render_template("Languages/Syntax/C#.html")
@app.route('/html', methods=['GET', 'POST'])
@login_required
def html():
    return render_template("Languages/Syntax/HTML.html")
@app.route('/java', methods=['GET', 'POST'])
@login_required
def java():
    return render_template("Languages/Syntax/Java.html")
@app.route('/javascript', methods=['GET', 'POST'])
@login_required
def javascript():
    return render_template("Languages/Syntax/JavaScript.html")
@app.route('/data_structures', methods=['GET', 'POST'])
@login_required
def data_structures():
    return render_template("Languages/Topics/DataStructures/DataStructures.html")
@app.route('/databases', methods=['GET', 'POST'])
@login_required
def databases():
    return render_template("Languages/Topics/Databases/Databases.html")
@app.route('/graphics', methods=['GET', 'POST'])
@login_required
def graphics():
    return render_template("Languages/Topics/Graphics/Graphics.html")
@app.route('/sql_database', methods=['GET', 'POST'])
@login_required
def sql_database():
    return render_template("Languages/Topics/Databases/SQL_Database.html")
@app.route('/python_ds', methods=['GET', 'POST'])
@login_required
def python_ds():
    return render_template("Languages/Topics/DataStructures/Python_DS.html")
@app.route('/java_ds', methods=['GET', 'POST'])
@login_required
def java_ds():
    return render_template("Languages/Topics/DataStructures/Java_DS.html")
@app.route('/c_plus_plus_ds', methods=['GET', 'POST'])
@login_required
def c_plus_plus_ds():
    return render_template("Languages/Topics/DataStructures/C_Plus_Plus_DS.html")
@app.route('/python_db', methods=['GET', 'POST'])
@login_required
def python_db():
    return render_template("Languages/Topics/Databases/Python_DB.html")
@app.route('/java_db', methods=['GET', 'POST'])
@login_required
def java_db():
    return render_template("Languages/Topics/Databases/Java_DB.html")
@app.route('/c_plus_plus_db', methods=['GET', 'POST'])
@login_required
def c_plus_plus_db():
    return render_template("Languages/Topics/Databases/C_Plus_Plus_DB.html")
@app.route('/python_graphics', methods=['GET', 'POST'])
@login_required
def python_graphics():
    return render_template("Languages/Topics/Graphics/Python_Graphics.html")
@app.route('/java_graphics', methods=['GET', 'POST'])
@login_required
def java_graphics():
    return render_template("Languages/Topics/Graphics/Java_Graphics.html")
@app.route('/c_plus_plus_graphics', methods=['GET', 'POST'])
@login_required
def c_plus_plus_graphics():
    return render_template("Languages/Topics/Graphics/c_plus_plus_graphics.html")