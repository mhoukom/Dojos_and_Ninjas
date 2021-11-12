from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninjas/new")
def new_ninja():
    all_dojos = Dojo.get_all()

    return render_template("new_ninja.html", all_dojos = all_dojos)


@app.route("/ninjas/create", methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)

    return redirect("/dojos")