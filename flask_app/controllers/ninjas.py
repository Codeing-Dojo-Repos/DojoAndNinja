from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = {
        'first_name':request.form['fname'],
        'last_name':request.form['lname'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    Ninja.create(data)
    return redirect('/dojos')

@app.route('/ninjas/new')
def create_ninja_form():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/ninjas/readAll/<int:id>')
def get_ninjas_by_dojo_id(id):
    print('hit get injas by id route...')
    data = {
        'id':id
    }
    ninjas = Ninja.get_ninjas_by_dojo_id(data)
    print(f'Ninjas: {ninjas}')
    return render_template('ninjas.html', ninjas=ninjas)
