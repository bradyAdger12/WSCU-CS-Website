from flask import render_template, request
from package import app
from flask_login import login_required
@app.route('/javaDataStructures', methods=['GET', 'POST'])
@login_required
def java_ds_select():
    structure = request.form.get("structureDropdown")
    if structure == "Array":
      return render_template("Languages/Topics/DataStructures/Java_DS/Array.html")
    if structure == "ArrayList":
      return render_template("Languages/Topics/DataStructures/Java_DS/ArrayList.html")
