from flask import render_template, request, flash, redirect, url_for

from app import app, db
from app.age_helper import AgeHelper
from app.controller import PostController


@app.route('/' )
def index():
    controller = PostController(db.session)
    post = controller.get_all_data()
    return render_template('index.html', post=post)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        controller = PostController(db.session)
        controller.add_new_data(request.form['title'], request.form['body'])
        flash('New entry was successfully posted')
    return render_template('add.html')

@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    controller = PostController(db.session)
    if request.method == 'POST':
        controller.edit_data_by_id(id,request.form['title'],request.form['body'])
        return redirect(url_for('index'))
    return render_template('edit.html', post=controller.get_data_by_id(id))

@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    controller = PostController(db.session)
    controller.delete_data_by_id(id)
    flash('deleted')

    return redirect(url_for('index'))