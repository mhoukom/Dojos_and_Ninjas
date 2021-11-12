from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route("/dojos")
def index():
    all_dojos = Dojo.get_all()

    return render_template("index.html", all_dojos = all_dojos)


@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    Dojo.create(request.form["name"])

    return redirect("/dojos")


@app.route("/dojos/<name>")
def display_dojo(name):
    return render_template("ninjas.html", dojo = Dojo.get_one(name))