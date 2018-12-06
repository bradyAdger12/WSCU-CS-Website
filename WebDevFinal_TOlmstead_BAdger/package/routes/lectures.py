from package import app
from flask import render_template
from flask_login import login_required
#C++ Content routes
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
#HTML Content routes
@app.route('/html_getting_started', methods=['GET', 'POST'])
@login_required
def html_getting_started():
    return render_template("Languages/HTML_Content/GettingStarted.html")
@app.route('/html_box_model', methods=['GET', 'POST'])
@login_required
def html_box_model():
    return render_template("Languages/HTML_Content/BoxModel.html")
@app.route('/html_css_basics', methods=['GET', 'POST'])
@login_required
def html_css_basics():
    return render_template("Languages/HTML_Content/CSS_Basics.html")
@app.route('/html_flask_databases', methods=['GET', 'POST'])
@login_required
def html_flask_databases():
    return render_template("Languages/HTML_Content/FlaskDatabases.html")
@app.route('/html_flask_routes', methods=['GET', 'POST'])
@login_required
def html_flask_routes():
    return render_template("Languages/HTML_Content/FlaskRoutes.html")
@app.route('/html_forms', methods=['GET', 'POST'])
@login_required
def html_forms():
    return render_template("Languages/HTML_Content/Forms.html")
@app.route('/html_hosting_and_images', methods=['GET', 'POST'])
@login_required
def html_hosting_and_images():
    return render_template("Languages/HTML_Content/HostingAndImages.html")
@app.route('/html_layouts_and_positioning', methods=['GET', 'POST'])
@login_required
def html_layouts_and_positioning():
    return render_template("Languages/HTML_Content/LayoutsAndPositioning.html")
@app.route('/html_tables', methods=['GET', 'POST'])
@login_required
def html_tables():
    return render_template("Languages/HTML_Content/Tables.html")
#JavaScript Content Routes
@app.route('/js_hello', methods=['GET', 'POST'])
@login_required
def js_hello():
    return render_template("Languages/JS_Content/HelloJavaScript.html")
@app.route('/js_2', methods=['GET', 'POST'])
@login_required
def js_2():
    return render_template("Languages/JS_Content/JavaScript2.html")
@app.route('/js_dom', methods=['GET', 'POST'])
@login_required
def js_dom():
    return render_template("Languages/JS_Content/JS3_DOM.html")
@app.route('/js_events', methods=['GET', 'POST'])
@login_required
def js_events():
    return render_template("Languages/JS_Content/JS3_Events.html")
#C++ Data Structures Routes
@app.route('/vectors', methods=['GET', 'POST'])
@login_required
def vectors():
    return render_template("Languages/CPP_Content/Vectors.html")
@app.route('/maps', methods=['GET', 'POST'])
@login_required
def maps():
    return render_template("Languages/CPP_Content/Maps.html")
#C++ Graphics
@app.route('/of_graphics', methods=['GET', 'POST'])
@login_required
def of_graphics():
    return render_template("Languages/CPP_Content/OFGraphics.html")
@app.route('/of_events', methods=['GET', 'POST'])
@login_required
def of_events():
    return render_template("Languages/CPP_Content/OFEvents.html")
@app.route('/of_sound', methods=['GET', 'POST'])
@login_required
def of_sound():
    return render_template("Languages/CPP_Content/OFSound.html")