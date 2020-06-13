import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Python Web..!!"

@app.route("/osahon")
def osahon():
    name = "Osahon"
    return render_template("osahon.html", name=name)

@app.route("/newmonth")
def newmonth():
    now = datetime.datetime.now()
    newmonth = now.day == 1
    return render_template("newmonth.html", newmonth = newmonth,name="NewMonth")