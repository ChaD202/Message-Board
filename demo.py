from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])

def HelloWorld():

    if request.method == "POST":
        name = request.form.get("enterName")
        email = request.form.get("enterEmail")
        add(name, email)

    return render_template("main.html")

def add(username, email):
    connection = sqlite3.connect("emails.db")

    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users(Username, Email) VALUES ('{u}', '{e}')".format(u=username, e=email))

    connection.commit()

@app.route('/page')

def page():
    return render_template("page.html")
