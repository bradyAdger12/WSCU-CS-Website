from flask import render_template, redirect, request, url_for
#from package.routes.lectures import *
from package import app
from flask_login import login_required

@app.route('/python', methods=['GET', 'POST'])
@login_required
def python():
    return render_template("Languages/Syntax/Python.html")
@app.route('/c_plus_plus', methods=['GET', 'POST'])
@login_required
def c_plus_plus():
    if request.method == 'POST':
        select_lecture = request.form['cpp_select']
        if select_lecture == "variables":
            return redirect(url_for('cpp_variables'))
        elif select_lecture == "flow_control":
            return redirect(url_for('cpp_flow_control'))
        elif select_lecture == "file_io":
            return redirect(url_for('cpp_fileIO'))
        elif select_lecture == "functions":
            return redirect(url_for('cpp_functions'))
        elif select_lecture == "pointers_and_new":
            return redirect(url_for('cpp_pointers'))
        elif select_lecture == "structs_and_classes":
            return redirect(url_for('cpp_structs_and_classes'))
        elif select_lecture == "pointers":
            return redirect(url_for('cpp_pointers'))
    return render_template("Languages/Syntax/C++.html")
@app.route('/c_sharp', methods=['GET', 'POST'])
@login_required
def c_sharp():
    return render_template("Languages/Syntax/C#.html")
@app.route('/html', methods=['GET', 'POST'])
@login_required
def html():
    if request.method == 'POST':
        select_lecture = request.form['html_select']
        if select_lecture == 'getting_started':
            return redirect(url_for('html_getting_started'))
        elif select_lecture == 'hosting_images':
            return redirect(url_for('html_hosting_and_images'))
        elif select_lecture == 'css basics':
            return redirect(url_for('html_css_basics'))
        elif select_lecture == 'Box Model':
            return redirect(url_for('html_box_model'))
        elif select_lecture == 'layouts':
            return redirect(url_for('html_layouts_and_positioning'))
        elif select_lecture == 'tables':
            return redirect(url_for('html_tables'))
        elif select_lecture == 'forms':
            return redirect(url_for('html_forms'))
        elif select_lecture == 'flask1':
            return redirect(url_for('html_flask_routes'))
        elif select_lecture == 'flask2':
            return redirect(url_for('html_flask_databases'))
    return render_template("Languages/Syntax/HTML.html")
@app.route('/java', methods=['GET', 'POST'])
@login_required
def java():
    return render_template("Languages/Syntax/Java.html")
@app.route('/javascript', methods=['GET', 'POST'])
@login_required
def javascript():
    if request.method == 'POST':
        form = request.form['js_select']
        if form == 'helloJS':
            return redirect(url_for('js_hello'))
        elif form == 'js2':
            return redirect(url_for('js_2'))
        elif form == 'domJS':
            return redirect(url_for('js_dom'))
        elif form == 'eventsJS':
            return redirect(url_for('js_events'))
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
    return render_template("Languages/Topics/DataStructures/Java_DS/Java_DS.html")
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