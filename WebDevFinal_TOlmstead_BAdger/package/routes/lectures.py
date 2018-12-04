from package import app
from flask import render_template
from flask_login import login_required

@app.route('/cpp_variables', methods=['GET', 'POST'])
@login_required
def cpp_variables():
    return render_template("Languages/CPP_Content/Variables.html")
@app.route('/cpp_flow_control', methods=['GET', 'POST'])
@login_required
def cpp_flow_control():
    return render_template("Languages/CPP_Content/FlowControl.html")
@app.route('/cpp_fileIO', methods=['GET', 'POST'])
@login_required
def cpp_fileIO():
    return render_template("Languages/CPP_Content/FileIO.html")
@app.route('/cpp_functions', methods=['GET', 'POST'])
@login_required
def cpp_functions():
    return render_template("Languages/CPP_Content/Functions.html")
@app.route('/cpp_structs_and_classes', methods=['GET', 'POST'])
@login_required
def cpp_structs_and_classes():
    return render_template("Languages/CPP_Content/StructsAndClasses.html")
@app.route('/cpp_pointers', methods=['GET', 'POST'])
@login_required
def cpp_pointers():
    return render_template("Languages/CPP_Content/Pointers.html")
