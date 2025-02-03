from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from flask import current_app as app

notes_data = [
    {"name": "Gitesh Pandey", "unit": "Unit 1-2"},
    {"name": "Sameer", "unit": "Unit 2-4"},
    {"name": "Afzal Jamal", "unit": "Unit 3-4"},
    {"name": "Manish Kashyap", "unit": "Unit 2-3"}
]

pyqs = [
    {"teacher": "Prof. Om Sir", "semester": "Semester 1", "year": "2020", "type" : "Cycle Test I"},
    {"teacher": "Prof. Om sir", "semester": "Semester 2", "year": "2019" , "type" : "Cycle Test II"},
    {"teacher": "Dr. Roy", "semester": "Semester 3", "year": "2021" , "type" : "Model Test"},
    {"teacher": "Prof. Iyer", "semester": "Semester 4", "year": "2018" , "type" : "Cycle Test I"},
    {"teacher": "Dr. Roy", "semester": "Semester 3", "year": "2021" , "type" : "Model Test"},
    {"teacher": "Prof. Om Sir", "semester": "Semester 4", "year": "2022" , "type" : "Cycle Test I"}
]


@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("user/home.html", current_user =  current_user)
    
    return render_template('user/home.html')

@app.route("/notes")
@login_required
def notes_page():
    return render_template("user/notes.html", notes = notes_data)


@app.route("/add-notes")
@login_required
def add_notes():
    return render_template("user/add_notes.html")


@app.route("/pyq")
@login_required
def pyq_page():
    return render_template("user/pyq.html", pyqs = pyqs)

@app.route("/add-pyq")
@login_required
def add_pyq():
    return render_template("user/add_pyq.html")


@app.route("/about")
def about():
    return render_template("user/about.html")