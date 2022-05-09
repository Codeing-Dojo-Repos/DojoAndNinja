from crypt import methods
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos():
    dojos =  Dojo.get_all()
    return render_template('index.html', dojos=dojos)

@app.route('/dojos/create', methods=["POST"])
def dojo_create():
    print(request.form)
    data = {
        "name":request.form['name']
    }
    Dojo.create(data)
    return redirect('/dojos')
